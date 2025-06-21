#!/usr/bin/env python3
"""
WSGI Entry Point for TaskFlow Pro
=================================
ملف دخول WSGI لنشر TaskFlow Pro على خوادم الإنتاج
"""

from app import create_app, db
import os

# إنشاء التطبيق للنشر
app = create_app()

# إنشاء قاعدة البيانات تلقائياً في البيئة الإنتاجية
with app.app_context():
    try:
        db.create_all()
        print("✅ Database tables created successfully")
    except Exception as e:
        print(f"⚠️ Database creation error: {e}")

if __name__ == "__main__":
    app.run()
