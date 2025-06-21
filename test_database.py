#!/usr/bin/env python3
"""
أداة اختبار قاعدة البيانات | Database Test Tool
تختبر الاتصال بقاعدة البيانات وتعرض معلومات مفصلة
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def test_database_connection():
    """اختبار الاتصال بقاعدة البيانات"""
    
    print("🔧 TaskFlow Pro - Database Connection Test")
    print("=" * 50)
    
    # الحصول على رابط قاعدة البيانات
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not set")
        print("💡 Set DATABASE_URL in your environment or .env file")
        return False
    
    # إخفاء كلمة المرور في العرض
    safe_url = database_url
    if '@' in database_url:
        parts = database_url.split('@')
        if ':' in parts[0]:
            user_part = parts[0].split(':')
            if len(user_part) > 1:
                safe_url = f"{user_part[0]}:***@{parts[1]}"
    
    print(f"🔗 Database URL: {safe_url}")
    
    # إصلاح تنسيق PostgreSQL
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
        print("🔧 Fixed postgres:// to postgresql://")
    
    try:
        # إنشاء محرك قاعدة البيانات
        print("🚀 Creating database engine...")
        engine = create_engine(database_url)
        
        # اختبار الاتصال
        print("🔌 Testing connection...")
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 as test"))
            test_value = result.fetchone()[0]
            
            if test_value == 1:
                print("✅ Database connection successful!")
                
                # اختبار إضافي - فحص الجداول
                try:
                    tables_result = connection.execute(text("""
                        SELECT table_name 
                        FROM information_schema.tables 
                        WHERE table_schema = 'public'
                    """))
                    tables = [row[0] for row in tables_result.fetchall()]
                    
                    if tables:
                        print(f"📋 Found {len(tables)} tables: {', '.join(tables)}")
                    else:
                        print("📋 No tables found (database is empty)")
                        
                except SQLAlchemyError as e:
                    print("⚠️ Could not fetch table information (might be SQLite)")
                
                return True
            else:
                print("❌ Database test query failed")
                return False
                
    except SQLAlchemyError as e:
        print(f"❌ Database connection failed: {e}")
        print("\n💡 Possible solutions:")
        print("   1. Check DATABASE_URL format")
        print("   2. Ensure database server is running")
        print("   3. Verify credentials and permissions")
        print("   4. Check network connectivity")
        return False
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_flask_app():
    """اختبار إنشاء تطبيق Flask"""
    
    print("\n🔧 Testing Flask App Creation")
    print("=" * 50)
    
    try:
        # إضافة مسار المشروع
        sys.path.insert(0, os.path.dirname(__file__))
        
        print("📦 Importing Flask app...")
        from app import create_app, db
        
        print("🚀 Creating Flask application...")
        app = create_app()
        
        print("🗄️ Testing database with Flask...")
        with app.app_context():
            db.create_all()
            print("✅ Flask app and database integration successful!")
            
        return True
        
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 TaskFlow Pro - Complete System Test")
    print("=" * 60)
    
    # اختبار قاعدة البيانات
    db_success = test_database_connection()
    
    # اختبار تطبيق Flask
    flask_success = test_flask_app()
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print(f"   Database Connection: {'✅ PASS' if db_success else '❌ FAIL'}")
    print(f"   Flask App Creation:  {'✅ PASS' if flask_success else '❌ FAIL'}")
    
    if db_success and flask_success:
        print("\n🎉 All tests passed! Your app should work correctly.")
        sys.exit(0)
    else:
        print("\n⚠️ Some tests failed. Check the errors above.")
        sys.exit(1)
