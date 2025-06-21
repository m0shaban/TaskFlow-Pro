"""
Helper functions for TaskFlow Pro
مساعدات نظام TaskFlow Pro
"""

def register_user_loader(login_manager):
    """Register the user loader function with the login manager"""
    from app.models import User
    
    @login_manager.user_loader
    def load_user(id):
        try:
            return User.query.get(int(id))
        except Exception:
            return None
    
    return load_user
