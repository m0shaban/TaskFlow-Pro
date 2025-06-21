from flask import render_template, redirect, url_for, flash, request, abort, jsonify
from flask_login import login_required, current_user
from app import db
from flask import Blueprint
from datetime import datetime

bp = Blueprint('main', __name__)
from app.main.forms import ProjectForm, TaskForm, RiskForm, TimeEntryForm
from app.models import Project, Task, Risk, RiskStatus, TimeEntry, TaskAssignment, User

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    projects = current_user.projects.all()
    project_count = current_user.projects.count()
    
    # Get assigned tasks if the user is not a manager/admin
    if current_user.is_manager():
        active_tasks = Task.query.join(Project).filter(
            Project.user_id == current_user.id,
            Task.completed == False
        ).count()
    else:
        active_tasks = Task.query.join(TaskAssignment).filter(
            TaskAssignment.user_id == current_user.id,
            Task.completed == False
        ).count()
    
    # Calculate completion rate
    total_tasks = Task.query.join(Project).filter(Project.user_id == current_user.id).count()
    completion_rate = 0
    if total_tasks > 0:
        completed_tasks = Task.query.join(Project).filter(
            Project.user_id == current_user.id,
            Task.completed == True
        ).count()
        completion_rate = int((completed_tasks / total_tasks) * 100)
    
    # Placeholder for recent activities - would be an Activity model in production
    recent_activity = []
    
    return render_template('main/index.html', 
                          title='Home', 
                          projects=projects,
                          project_count=project_count,
                          active_task_count=active_tasks,
                          completion_rate=completion_rate,
                          recent_activity=recent_activity)

@bp.route('/projects')
@login_required
def projects():
    if current_user.is_manager():
        projects = Project.query.filter_by(user_id=current_user.id).all()
    else:
        projects = Project.query.join(Task).join(TaskAssignment).filter(
            TaskAssignment.user_id == current_user.id
        ).distinct().all()
    
    return render_template('main/projects.html', title='Projects', projects=projects)

@bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if not current_user.is_manager():
        flash('You do not have permission to create projects.', 'danger')
        return redirect(url_for('main.index'))
        
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            budget=form.budget.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            owner=current_user
        )
        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
    return render_template('main/project_form.html', title='New Project', form=form)

@bp.route('/projects/<int:project_id>')
@login_required
def project(project_id):
    project = Project.query.get_or_404(project_id)
    if not current_user.is_manager() and not any(current_user in task.assigned_users() for task in project.tasks):
        abort(403)
    return render_template('main/project.html', title=project.name, project=project)

@bp.route('/projects/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
        
    form = ProjectForm()
    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.budget = form.budget.data
        project.start_date = form.start_date.data
        project.end_date = form.end_date.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
    elif request.method == 'GET':
        form.name.data = project.name
        form.description.data = project.description
        form.budget.data = project.budget
        form.start_date.data = project.start_date
        form.end_date.data = project.end_date
        
    return render_template('main/project_form.html', title='Edit Project', form=form, project=project)

@bp.route('/projects/<int:project_id>/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task(project_id):
    project = Project.query.get_or_404(project_id)
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
        
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            due_date=form.due_date.data,
            completed=form.completed.data,
            project=project
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
        
    return render_template('main/task_form.html', title='New Task', form=form, project=project)

@bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    project = task.project
    
    if project.owner != current_user and not current_user.is_admin() and current_user not in task.assigned_users():
        abort(403)
        
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.due_date = form.due_date.data
        task.completed = form.completed.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.priority.data = task.priority
        form.due_date.data = task.due_date
        form.completed.data = task.completed
        
    return render_template('main/task_form.html', title='Edit Task', form=form, task=task, project=project)

@bp.route('/tasks/<int:task_id>/assign', methods=['GET', 'POST'])
@login_required
def assign_task(task_id):
    task = Task.query.get_or_404(task_id)
    project = task.project
    
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
    
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                # Check if already assigned
                existing = TaskAssignment.query.filter_by(task_id=task.id, user_id=user.id).first()
                if not existing:
                    assignment = TaskAssignment(task=task, user=user)
                    db.session.add(assignment)
                    db.session.commit()
                    flash(f'Task assigned to {user.username}', 'success')
                else:
                    flash(f'User already assigned to this task', 'warning')
            else:
                flash('User not found', 'danger')
                
    # Get all users who could be assigned
    users = User.query.all()
    # Get current assignments
    current_assignments = TaskAssignment.query.filter_by(task_id=task.id).all()
    assigned_users = [a.user for a in current_assignments]
    
    return render_template('main/assign_task.html', 
                          title='Assign Task', 
                          task=task, 
                          users=users,
                          assigned_users=assigned_users)

@bp.route('/tasks/<int:task_id>/time_entries/new', methods=['GET', 'POST'])
@login_required
def new_time_entry(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Check permission - must be assigned to task or be project owner
    if task.project.owner != current_user and current_user not in task.assigned_users():
        abort(403)
        
    form = TimeEntryForm()
    if form.validate_on_submit():
        time_entry = TimeEntry(
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            billable=form.billable.data,
            user=current_user,
            task=task
        )
        db.session.add(time_entry)
        db.session.commit()
        flash('Time entry recorded successfully!', 'success')
        return redirect(url_for('main.project', project_id=task.project.id))
        
    return render_template('main/time_entry_form.html', 
                          title='New Time Entry', 
                          form=form, 
                          task=task)

@bp.route('/projects/<int:project_id>/risks/new', methods=['GET', 'POST'])
@login_required
def new_risk(project_id):
    project = Project.query.get_or_404(project_id)
    
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
        
    form = RiskForm()
    if form.validate_on_submit():
        risk = Risk(
            title=form.title.data,
            description=form.description.data,
            status=RiskStatus[form.status.data],
            due_date=form.due_date.data,
            mitigation_plan=form.mitigation_plan.data,
            project=project
        )
        db.session.add(risk)
        db.session.commit()
        flash('Risk added successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
        
    return render_template('main/risk_form.html', 
                          title='New Risk', 
                          form=form, 
                          project=project)

@bp.route('/reports/projects')
@login_required
def project_reports():
    if not current_user.is_manager():
        abort(403)
        
    projects = current_user.projects.all()
    return render_template('main/project_reports.html', 
                          title='Project Reports',
                          projects=projects)

@bp.route('/reports/time')
@login_required
def time_reports():
    if current_user.is_manager():
        # For managers, show time entries for their projects
        time_entries = TimeEntry.query.join(Task).join(Project).filter(
            Project.user_id == current_user.id
        ).order_by(TimeEntry.start_time.desc()).all()
    else:
        # For regular users, show their own time entries
        time_entries = current_user.time_entries.order_by(TimeEntry.start_time.desc()).all()
        
    return render_template('main/time_reports.html',
                          title='Time Reports',
                          time_entries=time_entries)
