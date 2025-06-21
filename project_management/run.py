from app import create_app, db
from app.models import User, Project, Task, TimeEntry, Risk, Department, UserRole, TaskAssignment

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User, 
        'Project': Project, 
        'Task': Task,
        'TimeEntry': TimeEntry,
        'Risk': Risk,
        'Department': Department,
        'UserRole': UserRole,
        'TaskAssignment': TaskAssignment
    }

if __name__ == '__main__':
    app.run(debug=True)
