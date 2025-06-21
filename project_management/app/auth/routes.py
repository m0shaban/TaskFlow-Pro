from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from werkzeug.urls import url_parse

bp = Blueprint('auth', __name__)
from app.auth.forms import LoginForm, RegistrationForm, UserEditForm
from app.models import User, UserRole, Department

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        flash(f'Welcome, {user.username}!', 'success')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    
    # Get departments for dropdown
    form.department.choices = [(d.id, d.name) for d in Department.query.all()]
    
    if form.validate_on_submit():
        user = User(
            username=form.username.data, 
            email=form.email.data,
            role=UserRole.USER
        )
        user.set_password(form.password.data)
        
        # Assign department if selected
        if form.department.data:
            department = Department.query.get(form.department.data)
            if department:
                user.department = department
        
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/users')
@login_required
def users():
    if not current_user.is_admin():
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('main.index'))
        
    users = User.query.all()
    return render_template('auth/users.html', title='Users', users=users)

@bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin() and current_user.id != user_id:
        flash('You do not have permission to edit this user.', 'danger')
        return redirect(url_for('main.index'))
        
    user = User.query.get_or_404(user_id)
    form = UserEditForm()
    
    # Only admin can change roles
    if current_user.is_admin():
        form.role.choices = [(role.name, role.value) for role in UserRole]
    else:
        del form.role
        
    # Get departments for dropdown
    form.department.choices = [(d.id, d.name) for d in Department.query.all()]
    form.department.choices.insert(0, (0, 'None'))
    
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        
        if current_user.is_admin() and form.role.data:
            user.role = UserRole[form.role.data]
            
        if form.department.data != 0:
            department = Department.query.get(form.department.data)
            if department:
                user.department = department
        else:
            user.department = None
            
        if form.password.data:
            user.set_password(form.password.data)
            
        db.session.commit()
        flash('User information updated successfully!', 'success')
        return redirect(url_for('auth.users'))
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        if current_user.is_admin():
            form.role.data = user.role.name
        if user.department:
            form.department.data = user.department.id
            
    return render_template('auth/user_edit.html', title='Edit User', form=form, user=user)
