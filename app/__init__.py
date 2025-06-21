from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'auth.login'  # Set after init_app
    csrf.init_app(app)  # Initialize CSRF protection

    # Make current_app available in templates
    @app.context_processor
    def inject_current_app():
        return dict(current_app=current_app)    # Import models after app creation to avoid circular imports
    from app import models
    
    # Register user loader after models are imported
    from app.utils import register_user_loader
    register_user_loader(login)

    # Register auth blueprint
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # Register main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Try to register API blueprint if it exists
    try:
        from app.api import bp as api_bp
        app.register_blueprint(api_bp, url_prefix='/api')
    except ImportError:
        pass
    
    # Try to register errors blueprint if it exists
    try:
        from app.errors import bp as errors_bp
        app.register_blueprint(errors_bp)
    except ImportError:
        pass

    return app
