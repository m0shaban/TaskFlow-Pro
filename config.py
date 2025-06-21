import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # TaskFlow Pro Configuration
    APP_NAME = 'TaskFlow Pro'
    APP_DESCRIPTION = 'نظام إدارة المشاريع والمهام المتطور'
    VERSION = '1.0.0'
    
    # Security Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'taskflow-pro-secret-key-2025'
      # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Fix for PostgreSQL URL format on Render
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Authentication Configuration
    LOGIN_DISABLED = False
    
    # Mail Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Application Configuration
    ITEMS_PER_PAGE = 10
    MAX_UPLOAD_SIZE = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    
    @staticmethod
    def init_app(app):
        pass
