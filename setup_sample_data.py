#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TaskFlow Pro - Initial Setup Script
===================================
سكريبت إعداد البيانات الأولية لنظام TaskFlow Pro

هذا السكريبت يقوم بإنشاء:
- مستخدم مدير افتراضي
- أقسام عينة
- مشروع تجريبي
- مهام عينة
"""

from app import create_app, db
from app.models import User, Department, Project, Task, UserRole
from datetime import datetime, timedelta

def create_sample_data():
    """إنشاء بيانات عينة للتطبيق"""
    
    app = create_app()
    
    with app.app_context():
        # إنشاء الجداول إذا لم تكن موجودة
        db.create_all()
        
        print("🚀 بدء إنشاء البيانات الأولية لـ TaskFlow Pro...")
        
        # 1. إنشاء الأقسام
        departments_data = [
            {"name": "تطوير البرمجيات", "description": "قسم تطوير التطبيقات والأنظمة"},
            {"name": "التسويق الرقمي", "description": "قسم التسويق الإلكتروني والمحتوى"},
            {"name": "إدارة المشاريع", "description": "قسم تخطيط وإدارة المشاريع"},
            {"name": "الموارد البشرية", "description": "قسم شؤون الموظفين والتوظيف"},
            {"name": "المالية والمحاسبة", "description": "قسم الشؤون المالية والمحاسبية"}
        ]
        
        departments = {}
        for dept_data in departments_data:
            if not Department.query.filter_by(name=dept_data["name"]).first():
                dept = Department(name=dept_data["name"], description=dept_data["description"])
                db.session.add(dept)
                departments[dept_data["name"]] = dept
                print(f"✅ تم إنشاء قسم: {dept_data['name']}")
        
        db.session.commit()
        
        # إعادة جلب الأقسام بعد الحفظ
        for dept_name in departments:
            departments[dept_name] = Department.query.filter_by(name=dept_name).first()
        
        # 2. إنشاء المستخدمين
        users_data = [
            {
                "username": "admin",
                "email": "admin@taskflow.pro",
                "password": "admin123",
                "role": UserRole.ADMIN,
                "department": "إدارة المشاريع"
            },
            {
                "username": "mohammed_dev",
                "email": "mohammed@taskflow.pro", 
                "password": "dev123",
                "role": UserRole.MANAGER,
                "department": "تطوير البرمجيات"
            },
            {
                "username": "sara_marketing",
                "email": "sara@taskflow.pro",
                "password": "marketing123", 
                "role": UserRole.USER,
                "department": "التسويق الرقمي"
            },
            {
                "username": "ahmed_hr",
                "email": "ahmed@taskflow.pro",
                "password": "hr123",
                "role": UserRole.USER, 
                "department": "الموارد البشرية"
            }
        ]
        
        users = {}
        for user_data in users_data:
            if not User.query.filter_by(username=user_data["username"]).first():
                user = User(
                    username=user_data["username"],
                    email=user_data["email"],
                    role=user_data["role"],
                    department=departments.get(user_data["department"])
                )
                user.set_password(user_data["password"])
                db.session.add(user)
                users[user_data["username"]] = user
                print(f"👤 تم إنشاء مستخدم: {user_data['username']} ({user_data['role'].value})")
        
        db.session.commit()
        
        # إعادة جلب المستخدمين بعد الحفظ
        for username in users:
            users[username] = User.query.filter_by(username=username).first()
        
        # 3. إنشاء المشاريع
        projects_data = [
            {
                "name": "تطوير نظام TaskFlow Pro",
                "description": "مشروع تطوير نظام إدارة المشاريع والمهام المتطور",
                "budget": 50000.0,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=90),
                "owner": "admin"
            },
            {
                "name": "حملة التسويق الرقمي 2025",
                "description": "حملة شاملة للتسويق الرقمي وزيادة الوعي بالعلامة التجارية",
                "budget": 25000.0,
                "start_date": datetime.now() + timedelta(days=7),
                "end_date": datetime.now() + timedelta(days=60),
                "owner": "sara_marketing"
            },
            {
                "name": "تحديث نظام الموارد البشرية",
                "description": "تحديث وتطوير نظام إدارة شؤون الموظفين",
                "budget": 30000.0,
                "start_date": datetime.now() + timedelta(days=14),
                "end_date": datetime.now() + timedelta(days=120),
                "owner": "ahmed_hr"
            }
        ]
        
        projects = {}
        for proj_data in projects_data:
            if not Project.query.filter_by(name=proj_data["name"]).first():
                project = Project(
                    name=proj_data["name"],
                    description=proj_data["description"],
                    budget=proj_data["budget"],
                    start_date=proj_data["start_date"],
                    end_date=proj_data["end_date"],
                    owner=users[proj_data["owner"]]
                )
                db.session.add(project)
                projects[proj_data["name"]] = project
                print(f"📁 تم إنشاء مشروع: {proj_data['name']}")
        
        db.session.commit()
        
        # إعادة جلب المشاريع بعد الحفظ
        for proj_name in projects:
            projects[proj_name] = Project.query.filter_by(name=proj_name).first()
        
        # 4. إنشاء المهام
        tasks_data = [
            {
                "title": "تصميم قاعدة البيانات",
                "description": "تصميم هيكل قاعدة البيانات للنظام",
                "priority": "high",
                "project": "تطوير نظام TaskFlow Pro",
                "due_date": datetime.now() + timedelta(days=7)
            },
            {
                "title": "تطوير واجهة المستخدم",
                "description": "تصميم وتطوير واجهة المستخدم الرئيسية",
                "priority": "high",
                "project": "تطوير نظام TaskFlow Pro",
                "due_date": datetime.now() + timedelta(days=14)
            },
            {
                "title": "اختبار النظام",
                "description": "إجراء اختبارات شاملة للنظام",
                "priority": "medium",
                "project": "تطوير نظام TaskFlow Pro",
                "due_date": datetime.now() + timedelta(days=21)
            },
            {
                "title": "إنشاء المحتوى التسويقي",
                "description": "كتابة وتصميم المحتوى للحملة التسويقية",
                "priority": "high",
                "project": "حملة التسويق الرقمي 2025",
                "due_date": datetime.now() + timedelta(days=10)
            },
            {
                "title": "إعداد الحملات الإعلانية",
                "description": "إعداد وتشغيل الحملات الإعلانية على وسائل التواصل",
                "priority": "medium",
                "project": "حملة التسويق الرقمي 2025",
                "due_date": datetime.now() + timedelta(days=15)
            }
        ]
        
        for task_data in tasks_data:
            if not Task.query.filter_by(title=task_data["title"]).first():
                task = Task(
                    title=task_data["title"],
                    description=task_data["description"],
                    priority=task_data["priority"],
                    due_date=task_data["due_date"],
                    project=projects[task_data["project"]]
                )
                db.session.add(task)
                print(f"📋 تم إنشاء مهمة: {task_data['title']}")
        
        db.session.commit()
        
        print("\n🎉 تم إنشاء البيانات الأولية بنجاح!")
        print("\n📊 ملخص البيانات المُنشأة:")
        print(f"   👥 المستخدمين: {len(users_data)}")
        print(f"   🏢 الأقسام: {len(departments_data)}")
        print(f"   📁 المشاريع: {len(projects_data)}")
        print(f"   📋 المهام: {len(tasks_data)}")
        
        print("\n🔐 بيانات تسجيل الدخول:")
        print("   مدير النظام:")
        print("   اسم المستخدم: admin")
        print("   كلمة المرور: admin123")
        print("\n   مطور:")
        print("   اسم المستخدم: mohammed_dev") 
        print("   كلمة المرور: dev123")
        
        print(f"\n🌐 افتح المتصفح وانتقل إلى: http://localhost:5000")
        print("   لبدء استخدام TaskFlow Pro!")

if __name__ == "__main__":
    create_sample_data()
