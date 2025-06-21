from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

class UserRole(Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    users = db.relationship('User', backref='department', lazy='dynamic')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.USER, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    assigned_tasks = db.relationship('TaskAssignment', back_populates='user')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def is_admin(self):
        return self.role == UserRole.ADMIN
        
    def is_manager(self):
        return self.role == UserRole.MANAGER or self.role == UserRole.ADMIN

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    budget = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy='dynamic')
    risks = db.relationship('Risk', backref='project', lazy='dynamic')
    resources = db.relationship('Resource', backref='project', lazy='dynamic')
    attachments = db.relationship('Attachment', backref='project', lazy='dynamic')
    
    def task_completion_rate(self):
        """Calculate the percentage of completed tasks in the project"""
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.tasks.filter_by(completed=True).count()
        return int((completed_tasks / total_tasks) * 100)
    
    def total_time_spent(self):
        """Calculate total time spent on this project's tasks in hours"""
        from sqlalchemy import func
        result = db.session.query(
            func.sum(func.julianday(TimeEntry.end_time) - func.julianday(TimeEntry.start_time)) * 24
        ).join(Task).filter(Task.project_id == self.id).scalar()
        return result or 0

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    priority = db.Column(db.String(10), default='medium', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    time_entries = db.relationship('TimeEntry', backref='task', lazy='dynamic')
    assignments = db.relationship('TaskAssignment', back_populates='task')
    risks = db.relationship('Risk', backref='task', lazy='dynamic')

class TaskAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user = db.relationship('User', back_populates='assigned_tasks')
    task = db.relationship('Task', back_populates='assignments')

class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    billable = db.Column(db.Boolean, default=True, nullable=False)

class RiskStatus(Enum):
    OPEN = 'open'
    IN_PROGRESS = 'in_progress'
    RESOLVED = 'resolved'
    CLOSED = 'closed'

class Risk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    status = db.Column(db.Enum(RiskStatus), default=RiskStatus.OPEN, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    mitigation_plan = db.Column(db.String(1000))

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50))  # task, project, risk, etc.
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(200))  # URL to related content

class Resource(db.Model):
    """Resource model for tracking resources allocated to projects"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # human, material, equipment
    cost_per_hour = db.Column(db.Float, default=0.0)
    availability = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

class Attachment(db.Model):
    """Model for file attachments (documents, images, etc.)"""
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)