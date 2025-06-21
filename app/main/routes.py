from flask import render_template, redirect, url_for, flash, request, abort, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import bp
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from app.main.forms import ProjectForm, TaskForm, RiskForm, TimeEntryForm, DepartmentForm
from app.models import User, Project, Task, TaskAssignment, Risk, Department, UserRole, RiskStatus, TimeEntry

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    # Calculate dashboard metrics
    project_count = Project.query.filter_by(user_id=current_user.id).count() if current_user.is_manager() else 0
    
    # Get active tasks assigned to the user
    if current_user.is_manager():
        active_task_count = Task.query.join(Project).filter(
            Project.user_id == current_user.id,
            Task.completed == False
        ).count()
    else:
        active_task_count = Task.query.join(TaskAssignment).filter(
            TaskAssignment.user_id == current_user.id,
            Task.completed == False
        ).count()
    
    # Calculate completion rate
    total_tasks = 0
    completed_tasks = 0
    
    if current_user.is_manager():
        projects = Project.query.filter_by(user_id=current_user.id).all()
        for project in projects:
            total_tasks += project.tasks.count()
            completed_tasks += project.tasks.filter_by(completed=True).count()
    else:
        task_ids = [assignment.task_id for assignment in current_user.assigned_tasks]
        total_tasks = len(task_ids)
        completed_tasks = Task.query.filter(Task.id.in_(task_ids), Task.completed == True).count() if task_ids else 0
    
    completion_rate = int((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0)
    
    # Get projects to display on dashboard
    projects = Project.query.filter_by(user_id=current_user.id).all() if current_user.is_manager() else []
    
    # Placeholder for recent activities
    recent_activity = []
    # You could get actual activities from database if you have an Activity model
    
    return render_template('main/index.html', 
                          title='Dashboard',
                          project_count=project_count,
                          active_task_count=active_task_count,
                          completion_rate=completion_rate,
                          projects=projects,
                          recent_activity=recent_activity)

@bp.route('/projects')
@login_required
def projects():
    if current_user.is_manager():
        projects = Project.query.filter_by(user_id=current_user.id).all()
    else:
        # For regular users, get only projects where they have assigned tasks
        assigned_project_ids = db.session.query(Project.id).join(Task).join(TaskAssignment).filter(
            TaskAssignment.user_id == current_user.id
        ).distinct().all()
        project_ids = [p[0] for p in assigned_project_ids]
        projects = Project.query.filter(Project.id.in_(project_ids)).all()
    
    return render_template('main/projects.html', 
                          title='Projects',
                          projects=projects,
                          now=datetime.utcnow())

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
            user_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
    return render_template('main/project_form.html', title='New Project', form=form)

@bp.route('/projects/<int:project_id>')
@login_required
def project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.owner != current_user and not current_user.is_admin():
        # Check if user is assigned to any task in this project
        is_assigned = False
        for task in project.tasks:
            for assignment in task.assignments:
                if assignment.user_id == current_user.id:
                    is_assigned = True
                    break
            if is_assigned:
                break
        
        if not is_assigned:
            flash('You do not have permission to view this project.', 'danger')
            return redirect(url_for('main.projects'))
            
    return render_template('main/project.html', title=project.name, project=project)

@bp.route('/projects/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    # Check permission
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
    
    # Check permission
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
            project_id=project.id
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
    
    # Check permissions
    if project.owner != current_user and not current_user.is_admin():
        # Check if user is assigned to this task
        is_assigned = False
        for assignment in task.assignments:
            if assignment.user_id == current_user.id:
                is_assigned = True
                break
                
        if not is_assigned:
            flash('You do not have permission to edit this task.', 'danger')
            return redirect(url_for('main.projects'))
        
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

@bp.route('/tasks/<int:task_id>/time_entries/new', methods=['GET', 'POST'])
@login_required
def new_time_entry(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Check permission
    is_assigned = False
    for assignment in task.assignments:
        if assignment.user_id == current_user.id:
            is_assigned = True
            break
            
    if task.project.owner != current_user and not current_user.is_admin() and not is_assigned:
        abort(403)
    
    form = TimeEntryForm()
    if form.validate_on_submit():
        time_entry = TimeEntry(
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            billable=form.billable.data,
            user_id=current_user.id,
            task_id=task.id
        )
        db.session.add(time_entry)
        db.session.commit()
        flash('Time entry recorded successfully!', 'success')
        return redirect(url_for('main.project', project_id=task.project.id))
        
    return render_template('main/time_entry_form.html',
                          title='Record Time',
                          form=form,
                          task=task)

@bp.route('/tasks/<int:task_id>/assign', methods=['GET', 'POST'])
@login_required
def assign_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Check permission
    if task.project.owner != current_user and not current_user.is_admin():
        abort(403)
    
    # Handle form submission
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                # Check if already assigned
                existing = TaskAssignment.query.filter_by(task_id=task.id, user_id=user.id).first()
                if not existing:
                    assignment = TaskAssignment(task_id=task.id, user_id=user.id)
                    db.session.add(assignment)
                    db.session.commit()
                    flash(f'User {user.username} assigned to task successfully', 'success')
                else:
                    flash('User is already assigned to this task', 'warning')
            else:
                flash('User not found', 'danger')
    
    # Get all users for dropdown
    users = User.query.all()
    
    # Get currently assigned users
    assigned_users = []
    for assignment in task.assignments:
        assigned_users.append(assignment.user)
    
    return render_template('main/assign_task.html', 
                          title='Assign Task',
                          task=task,
                          users=users,
                          assigned_users=assigned_users)

@bp.route('/tasks/<int:task_id>/unassign/<int:user_id>', methods=['POST'])
@login_required
def unassign_task(task_id, user_id):
    task = Task.query.get_or_404(task_id)
    
    # Check permission
    if task.project.owner != current_user and not current_user.is_admin():
        abort(403)
    
    assignment = TaskAssignment.query.filter_by(task_id=task_id, user_id=user_id).first_or_404()
    db.session.delete(assignment)
    db.session.commit()
    
    flash('User unassigned from task successfully', 'success')
    return redirect(url_for('main.assign_task', task_id=task_id))

@bp.route('/my_tasks')
@login_required
def my_tasks():
    # Get all tasks assigned to current user
    tasks = TaskAssignment.query.filter_by(user_id=current_user.id).all()
    
    # For filtering in template
    now = datetime.utcnow()
    
    # Filter tasks into categories
    completed_tasks = [a for a in tasks if a.task.completed]
    in_progress_tasks = [a for a in tasks if not a.task.completed and (not a.task.due_date or a.task.due_date >= now)]
    overdue_tasks = [a for a in tasks if not a.task.completed and a.task.due_date and a.task.due_date < now]
    
    return render_template('main/assigned_tasks.html',
                          title='My Tasks',
                          tasks=tasks,
                          completed_tasks=completed_tasks,
                          in_progress_tasks=in_progress_tasks,
                          overdue_tasks=overdue_tasks,
                          now=now)

@bp.route('/risks')
@login_required
def risks():
    """Show all risks for manager/admin or related risks for normal users"""
    if current_user.is_manager():
        # For managers/admins, get all risks from their projects
        project_ids = [p.id for p in Project.query.filter_by(user_id=current_user.id).all()]
        risks = Risk.query.filter(Risk.project_id.in_(project_ids)).all() if project_ids else []
        projects = Project.query.filter_by(user_id=current_user.id).all()
    else:
        # For regular users, get risks from projects where they are assigned tasks
        assigned_projects = Project.query.join(Task).join(TaskAssignment).filter(
            TaskAssignment.user_id == current_user.id
        ).distinct().all()
        project_ids = [p.id for p in assigned_projects]
        risks = Risk.query.filter(Risk.project_id.in_(project_ids)).all() if project_ids else []
        projects = []
    
    # Create a basic form for CSRF protection
    form = FlaskForm()
    
    return render_template('main/risks.html', 
                          title='Risks Management',
                          risks=risks,
                          projects=projects,
                          form=form)

@bp.route('/projects/<int:project_id>/risks/new', methods=['GET', 'POST'])
@login_required
def new_risk(project_id):
    project = Project.query.get_or_404(project_id)
    
    # Check permission
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
            project_id=project.id
        )
        db.session.add(risk)
        db.session.commit()
        flash('Risk added successfully!', 'success')
        return redirect(url_for('main.project', project_id=project.id))
        
    return render_template('main/risk_form.html', 
                          title='New Risk', 
                          form=form, 
                          project=project)

@bp.route('/risks/<int:risk_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_risk(risk_id):
    risk = Risk.query.get_or_404(risk_id)
    project = risk.project
    
    # Check permission
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
    
    form = RiskForm()
    if form.validate_on_submit():
        risk.title = form.title.data
        risk.description = form.description.data
        risk.status = RiskStatus[form.status.data]
        risk.due_date = form.due_date.data
        risk.mitigation_plan = form.mitigation_plan.data
        
        db.session.commit()
        flash('Risk updated successfully!', 'success')
        return redirect(url_for('main.risks'))
    elif request.method == 'GET':
        form.title.data = risk.title
        form.description.data = risk.description
        form.status.data = risk.status.name
        form.due_date.data = risk.due_date
        form.mitigation_plan.data = risk.mitigation_plan
        
    return render_template('main/risk_form.html', 
                          title='Edit Risk',
                          form=form, 
                          risk=risk,
                          project=project)

@bp.route('/risks/<int:risk_id>/delete', methods=['POST'])
@login_required
def delete_risk(risk_id):
    risk = Risk.query.get_or_404(risk_id)
    project = risk.project
    
    # Check permission
    if project.owner != current_user and not current_user.is_admin():
        abort(403)
    
    form = FlaskForm()
    if form.validate_on_submit():
        db.session.delete(risk)
        db.session.commit()
        flash('Risk deleted successfully', 'success')
    else:
        flash('CSRF validation failed', 'danger')
        
    return redirect(url_for('main.risks'))

@bp.route('/reports/projects')
@login_required
def project_reports():
    if not current_user.is_manager():
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('main.index'))
        
    projects = Project.query.filter_by(user_id=current_user.id).all()
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
        time_entries = TimeEntry.query.filter_by(user_id=current_user.id).order_by(TimeEntry.start_time.desc()).all()
        
    return render_template('main/time_reports.html',
                          title='Time Reports',
                          time_entries=time_entries)

@bp.route('/reports/custom', methods=['GET', 'POST'])
@login_required
def custom_reports():
    """إنشاء تقارير مخصصة"""
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        metrics = request.form.getlist('metrics')
        projects = request.form.getlist('projects')
        
        # ... توليد التقرير المخصص
        
    return render_template('main/custom_reports.html',
                         title='تقارير مخصصة',
                         projects=current_user.projects)

# Department management
@bp.route('/departments')
@login_required
def departments():
    """Show departments and allow management for admins"""
    if not current_user.is_admin():
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('main.index'))
        
    departments = Department.query.all()
    return render_template('main/departments.html', title='Departments', departments=departments)

@bp.route('/departments/new', methods=['GET', 'POST'])
@login_required
def new_department():
    """Create a new department"""
    if not current_user.is_admin():
        flash('You do not have permission to create departments.', 'danger')
        return redirect(url_for('main.index'))
        
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(department)
        db.session.commit()
        flash('Department created successfully!', 'success')
        return redirect(url_for('main.departments'))
        
    return render_template('main/department_form.html', title='New Department', form=form)

@bp.route('/departments/<int:department_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_department(department_id):
    """Edit an existing department"""
    if not current_user.is_admin():
        flash('You do not have permission to edit departments.', 'danger')
        return redirect(url_for('main.index'))
        
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm()
    
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('Department updated successfully!', 'success')
        return redirect(url_for('main.departments'))
    elif request.method == 'GET':
        form.name.data = department.name
        form.description.data = department.description
        
    return render_template('main/department_form.html', title='Edit Department', form=form, department=department)

@bp.route('/departments/<int:department_id>/delete', methods=['POST'])
@login_required
def delete_department(department_id):
    """Delete a department"""
    if not current_user.is_admin():
        flash('You do not have permission to delete departments.', 'danger')
        return redirect(url_for('main.index'))
        
    department = Department.query.get_or_404(department_id)
    
    # Check if department has users
    if department.users.count() > 0:
        flash('Cannot delete department with assigned users.', 'danger')
        return redirect(url_for('main.departments'))
    
    db.session.delete(department)
    db.session.commit()
    flash('Department deleted successfully!', 'success')
    return redirect(url_for('main.departments'))

@bp.route('/settings')
@login_required
def settings():
    """System settings (admin only)"""
    if not current_user.is_admin():
        flash('You do not have permission to view system settings.', 'danger')
        return redirect(url_for('main.index'))
    
    return render_template('main/settings.html', title='System Settings')

@bp.route('/user/<username>')
@login_required
def user(username):
    """View user profile"""
    user = User.query.filter_by(username=username).first_or_404()
    # For template display
    now = datetime.utcnow()
    return render_template('main/user.html',
                          title=f'Profile: {username}',
                          user=user,
                          now=now)

@bp.route('/calendar')
@login_required
def calendar():
    """Show calendar with tasks and deadlines"""
    if current_user.is_manager():
        tasks = Task.query.join(Project).filter(Project.user_id == current_user.id).all()
    else:
        tasks = [assignment.task for assignment in current_user.assigned_tasks]
    
    return render_template('main/calendar.html', 
                         title='التقويم',
                         tasks=tasks)

@bp.route('/docs')
def documentation():
    """Documentation landing page"""
    return render_template('docs/landing.html', title='دليل الاستخدام')
