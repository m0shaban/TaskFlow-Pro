from app import create_app, db
from app.models import User, UserRole, Department

app = create_app()

def init_db():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Create departments
        departments = [
            Department(name="Engineering", description="Software development and engineering"),
            Department(name="Marketing", description="Marketing and communications"),
            Department(name="Finance", description="Financial management and accounting"),
            Department(name="HR", description="Human resources and talent management"),
            Department(name="Operations", description="Day-to-day business operations")
        ]
        
        # Check if admin user exists, if not create one
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            admin = User(
                username="admin",
                email="admin@example.com",
                role=UserRole.ADMIN
            )
            admin.set_password("admin123")  # Default admin password
            db.session.add(admin)
            print("Created admin user with username 'admin' and password 'admin123'")
        
        # Add departments that don't exist
        for dept in departments:
            existing = Department.query.filter_by(name=dept.name).first()
            if not existing:
                db.session.add(dept)
        
        db.session.commit()
        print("Database initialized with departments and admin user.")

if __name__ == "__main__":
    init_db()
