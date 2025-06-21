from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from wtforms.validators import Optional
from wtforms import SelectField

# Fix for the url_parse import
from urllib.parse import urlparse

bp = Blueprint('auth', __name__)
from app.auth.forms import LoginForm, RegistrationForm, UserEditForm
from app.models import User, UserRole, Department, TaskAssignment, TimeEntry, Task, Project, Risk

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password. Default admin credentials are username: "admin", password: "admin123"', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # Use urlparse instead of url_parse
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.index')
        flash(f'Welcome, {user.username}!', 'success')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    
    # Add department choices to the form
    departments = Department.query.all()
    if departments:
        form.department = SelectField('Department', coerce=int, choices=[(0, 'None')] + [(d.id, d.name) for d in departments], validators=[Optional()])
    
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role=UserRole.USER)
        user.set_password(form.password.data)
        
        # Assign department if selected and not None
        if hasattr(form, 'department') and form.department.data != 0:
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
    form = UserEditForm(original_username=user.username)
    
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

@bp.route('/users/<int:user_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin():
        flash('You do not have permission to delete users.', 'danger')
        return redirect(url_for('main.index'))
        
    user = User.query.get_or_404(user_id)
    
    # Prevent deleting yourself
    if user.id == current_user.id:
        flash('You cannot delete your own account.', 'danger')
        return redirect(url_for('auth.users'))
    
    try:
        # Remove user's task assignments
        TaskAssignment.query.filter_by(user_id=user.id).delete()
        
        # For user's projects, either reassign or delete
        for project in user.projects:
            if current_user.is_admin():
                # Reassign to current admin
                project.user_id = current_user.id
            else:
                # Or delete the project and related data
                Risk.query.filter_by(project_id=project.id).delete()
                
                for task in project.tasks:
                    TimeEntry.query.filter_by(task_id=task.id).delete()
                    Risk.query.filter_by(task_id=task.id).delete()
                    TaskAssignment.query.filter_by(task_id=task.id).delete()
                
                Task.query.filter_by(project_id=project.id).delete()
                db.session.delete(project)
        
        # Delete user's time entries
        TimeEntry.query.filter_by(user_id=user.id).delete()
        
        # Finally delete the user
        db.session.delete(user)
        db.session.commit()
        
        flash(f'User {user.username} has been deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting user: {str(e)}', 'danger')
    
    return redirect(url_for('auth.users'))
