from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, FloatField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    budget = FloatField('Budget', validators=[Optional(), NumberRange(min=0)])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[Optional()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Create Project')

class TaskForm(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    priority = SelectField('Priority', choices=[
        ('low', 'Low'),
        ('medium', 'Medium'), 
        ('high', 'High')
    ], validators=[DataRequired()])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[Optional()])
    completed = BooleanField('Completed')
    submit = SubmitField('Create Task')

class RiskForm(FlaskForm):
    title = StringField('Risk Title', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    status = SelectField('Status', choices=[
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed')
    ], validators=[DataRequired()])
    mitigation_plan = TextAreaField('Mitigation Plan', validators=[Length(max=1000)])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Submit Risk')

class TimeEntryForm(FlaskForm):
    description = TextAreaField('Description', validators=[Length(max=500)])
    start_time = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_time = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    billable = BooleanField('Billable')
    submit = SubmitField('Submit Time Entry')

class DepartmentForm(FlaskForm):
    name = StringField('Department Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    submit = SubmitField('Save Department')
