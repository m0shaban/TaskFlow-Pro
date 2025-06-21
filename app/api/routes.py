from flask import jsonify, request, url_for, abort
from app import db
from app.api import bp
from app.models import User, Project, Task, Risk, TimeEntry
from flask_login import current_user, login_required
from datetime import datetime, timedelta

@bp.route('/projects', methods=['GET'])
@login_required
def get_projects():
    if current_user.is_manager():
        projects = Project.query.filter_by(user_id=current_user.id).all()
    else:
        # For regular users, get only projects where they have assigned tasks
        projects = Project.query.join(Task).join('assignments').filter(
            User.id == current_user.id).distinct().all()
    
    return jsonify({
        'projects': [{'id': p.id, 'name': p.name, 'task_count': p.tasks.count()} for p in projects]
    })

@bp.route('/projects/<int:id>/tasks', methods=['GET'])
@login_required
def get_project_tasks(id):
    project = Project.query.get_or_404(id)
    
    # Check permission
    if project.user_id != current_user.id and not current_user.is_admin():
        tasks_assigned = Task.query.join('assignments').filter(
            Task.project_id == id,
            User.id == current_user.id
        ).count()
        if tasks_assigned == 0:
            abort(403)
    
    tasks = Task.query.filter_by(project_id=id).all()
    return jsonify({
        'tasks': [{'id': t.id, 'title': t.title, 'priority': t.priority, 'completed': t.completed} 
                 for t in tasks]
    })

@bp.route('/tasks/<int:id>/toggle-complete', methods=['POST'])
@login_required
def toggle_task_complete(id):
    task = Task.query.get_or_404(id)
    
    # Check permission
    if task.project.user_id != current_user.id and not current_user.is_admin():
        assigned = any(a.user_id == current_user.id for a in task.assignments)
        if not assigned:
            abort(403)
    
    task.completed = not task.completed
    db.session.commit()
    
    return jsonify({'success': True, 'completed': task.completed})

@bp.route('/reports/completion-rate', methods=['GET'])
@login_required
def completion_rate():
    # Default to last 30 days
    days = request.args.get('days', 30, type=int)
    
    # Get date range
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    if current_user.is_manager():
        # For project managers, get their projects
        projects = Project.query.filter_by(user_id=current_user.id).all()
        project_ids = [p.id for p in projects]
        total_tasks = Task.query.filter(
            Task.project_id.in_(project_ids),
            Task.created_at >= start_date
        ).count()
        completed_tasks = Task.query.filter(
            Task.project_id.in_(project_ids),
            Task.completed == True,
            Task.created_at >= start_date
        ).count()
    else:
        # For regular users, get assigned tasks
        assigned_task_ids = [a.task_id for a in current_user.assigned_tasks]
        total_tasks = Task.query.filter(
            Task.id.in_(assigned_task_ids),
            Task.created_at >= start_date
        ).count()
        completed_tasks = Task.query.filter(
            Task.id.in_(assigned_task_ids),
            Task.completed == True,
            Task.created_at >= start_date
        ).count()
    
    completion_rate = 0
    if total_tasks > 0:
        completion_rate = (completed_tasks / total_tasks) * 100
    
    return jsonify({
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'completion_rate': round(completion_rate, 2),
        'period_days': days
    })

@bp.route('/reports/time-summary', methods=['GET'])
@login_required
def time_summary():
    # Default to last 30 days
    days = request.args.get('days', 30, type=int)
    
    # Get date range
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    if current_user.is_manager():
        # For project managers, get time entries for all their projects
        projects = Project.query.filter_by(user_id=current_user.id).all()
        project_ids = [p.id for p in projects]
        
        time_entries = TimeEntry.query.join(Task).filter(
            Task.project_id.in_(project_ids),
            TimeEntry.start_time >= start_date
        ).all()
    else:
        # For regular users, get their own time entries
        time_entries = TimeEntry.query.filter(
            TimeEntry.user_id == current_user.id,
            TimeEntry.start_time >= start_date
        ).all()
    
    # Calculate total hours and billable hours
    total_hours = sum(entry.hours() for entry in time_entries)
    billable_hours = sum(entry.hours() for entry in time_entries if entry.billable)
    
    return jsonify({
        'total_hours': round(total_hours, 2),
        'billable_hours': round(billable_hours, 2),
        'entry_count': len(time_entries),
        'period_days': days
    })

@bp.route('/api/v1/statistics', methods=['GET'])
@login_required
def get_statistics():
    """إحصائيات شاملة للمشاريع والمهام"""
    return jsonify({
        'projects_count': Project.query.filter_by(user_id=current_user.id).count(),
        'active_tasks': Task.query.filter_by(completed=False).count(),
        'completion_rate': calculate_completion_rate(),
        'total_time': calculate_total_time()
    })
