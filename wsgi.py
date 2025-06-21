#!/usr/bin/env python3
"""
WSGI Entry Point for TaskFlow Pro
=================================
ملف دخول WSGI لنشر TaskFlow Pro على خوادم الإنتاج
"""

import os
import sys
import traceback
from flask import Flask

# إضافة مسار المشروع إلى sys.path
sys.path.insert(0, os.path.dirname(__file__))

# طباعة معلومات البيئة للتشخيص
print("🔧 TaskFlow Pro WSGI Initialization")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"WSGI file location: {__file__}")

# فحص المتغيرات البيئية الهامة
env_vars = ['SECRET_KEY', 'DATABASE_URL', 'FLASK_ENV']
print("\n📋 Environment Variables Check:")
for var in env_vars:
    value = os.environ.get(var)
    if value:
        # إخفاء القيم الحساسة جزئياً
        if var == 'SECRET_KEY':
            print(f"  {var}: {'*' * (len(value) - 4)}{value[-4:] if len(value) > 4 else '****'}")
        elif var == 'DATABASE_URL':
            print(f"  {var}: {value[:20]}...{value[-20:] if len(value) > 40 else value}")
        else:
            print(f"  {var}: {value}")
    else:
        print(f"  {var}: ❌ NOT SET")

# إنشاء التطبيق للنشر
try:
    print("\n🚀 Creating TaskFlow Pro application...")
    from app import create_app, db
    app = create_app()
    print("✅ TaskFlow Pro app created successfully")
    
    # إنشاء قاعدة البيانات تلقائياً في البيئة الإنتاجية
    with app.app_context():
        try:
            print("🗄️ Setting up database...")
            db.create_all()
            print("✅ Database tables created successfully")
        except Exception as e:
            print(f"⚠️ Database creation error: {e}")
            traceback.print_exc()
            
except Exception as e:
    print(f"❌ Error creating app: {e}")
    traceback.print_exc()
    
    # إنشاء تطبيق بسيط للتشخيص
    app = Flask(__name__)
    
    @app.route('/')
    def health_check():
        error_details = traceback.format_exc()
        return f"""
        <h1>TaskFlow Pro - Configuration Error</h1>
        <h2>Error: {str(e)}</h2>
        <h3>Environment Variables:</h3>
        <ul>
            <li>SECRET_KEY: {'✅' if os.environ.get('SECRET_KEY') else '❌'}</li>
            <li>DATABASE_URL: {'✅' if os.environ.get('DATABASE_URL') else '❌'}</li>
            <li>FLASK_ENV: {os.environ.get('FLASK_ENV', 'Not Set')}</li>
        </ul>
        <h3>Error Details:</h3>
        <pre>{error_details}</pre>
        """

if __name__ == "__main__":
    app.run()
