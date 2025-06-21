from app import create_app, db
import sqlite3
from app.models import Department, User

app = create_app()

def fix_database():
    with app.app_context():
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

if __name__ == "__main__":
    fix_database()
