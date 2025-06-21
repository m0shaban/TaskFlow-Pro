#!/usr/bin/env python3
"""
WSGI Entry Point for TaskFlow Pro
=================================
ملف دخول WSGI لنشر TaskFlow Pro على خوادم الإنتاج
"""

from app import create_app, db
import os

# إنشاء التطبيق للنشر
try:
    app = create_app()
    print("✅ TaskFlow Pro app created successfully")
    
    # إنشاء قاعدة البيانات تلقائياً في البيئة الإنتاجية
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database tables created successfully")
        except Exception as e:
            print(f"⚠️ Database creation error: {e}")
            
except Exception as e:
    print(f"❌ Error creating app: {e}")
    # إنشاء تطبيق بسيط للتشخيص
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def health_check():
        return f"TaskFlow Pro - Configuration Error: {str(e)}"

if __name__ == "__main__":
    app.run()
