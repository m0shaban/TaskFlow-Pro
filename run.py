from app import create_app, db
from app.models import User, Project, Task, TimeEntry, Risk, Department, UserRole, TaskAssignment
import sqlite3

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

@app.cli.command("create-tables")
def create_tables():
    """Create all database tables."""
    db.create_all()
    print("Database tables created.")

@app.cli.command("fix-database")
def fix_database():
    """Fix missing department_id column in user table."""
    # Get the database path from config
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    
    # Direct SQLite connection to add the missing column
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if department table exists, create if not
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='department'")
    if not cursor.fetchone():
        print("Creating department table...")
        cursor.execute("""
        CREATE TABLE department (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(500)
        )
        """)
    
    # Check if department_id column exists in user table
    cursor.execute("PRAGMA table_info(user)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'department_id' not in columns:
        print("Adding department_id column to user table...")
        cursor.execute("ALTER TABLE user ADD COLUMN department_id INTEGER")
    
    conn.commit()
    conn.close()
    
    # Create initial departments
    with app.app_context():
        departments = [
            Department(name="Engineering", description="Software development and engineering"),
            Department(name="Marketing", description="Marketing and communications"),
            Department(name="Finance", description="Financial management and accounting"),
            Department(name="HR", description="Human resources and talent management"),
            Department(name="Operations", description="Day-to-day business operations")
        ]
        
        for dept in departments:
            existing = Department.query.filter_by(name=dept.name).first()
            if not existing:
                db.session.add(dept)
        
        db.session.commit()
    
    print("Database fixed successfully.")

@app.cli.command("fix-migrations")
def fix_migrations():
    """Fix migrations with multiple heads by merging them."""
    from flask_migrate import current, merge_heads
    revisions = current(directory='migrations')
    if len(revisions) > 1:
        print(f"Found multiple heads: {revisions}")
        merge_heads('migrations', revisions)
        print("Heads merged. Run 'flask db upgrade' to apply migrations.")
    else:
        print("No multiple heads found.")

@app.cli.command("reset-migrations")
def reset_migrations():
    """Reset migrations by creating a fresh initial migration."""
    import os
    import shutil
    
    # Backup the database
    if os.path.exists('app.db'):
        shutil.copy('app.db', 'app.db.backup')
        print("Database backed up to app.db.backup")
    
    # Remove migrations folder
    if os.path.exists('migrations'):
        shutil.rmtree('migrations')
        print("Migrations folder removed")
    
    # Initialize migrations
    from flask_migrate import init, migrate, upgrade
    init('migrations')
    print("Migrations initialized")
    
    # Create migration
    migrate(message='Initial database setup')
    print("Initial migration created")
    
    # Apply migration
    upgrade()
    print("Migration applied")
    
    print("Migration reset complete")

if __name__ == '__main__':
    app.run(debug=True)
