# دليل تشخيص مشاكل النشر | Deployment Troubleshooting Guide

## مشاكل شائعة وحلولها | Common Issues and Solutions

### 1. Internal Server Error (500)

#### الأسباب المحتملة:
- **متغيرات البيئة مفقودة:** SECRET_KEY أو DATABASE_URL غير مضبوطين
- **خطأ في رابط قاعدة البيانات:** تنسيق DATABASE_URL خاطئ
- **مشكلة استيراد دوري:** Circular import في الكود
- **خطأ في الكود:** أخطاء برمجية في Python

#### خطوات التشخيص:

**1. فحص متغيرات البيئة في Render:**
```bash
# في Render Dashboard > Service > Environment
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@host:port/database
FLASK_ENV=production
```

**2. فحص سجل الأخطاء في Render:**
- اذهب إلى Dashboard > Service > Logs
- ابحث عن رسائل الخطأ والتشخيص

**3. التحقق من الإعداد المحلي:**
```bash
# في مجلد المشروع
python wsgi.py
# يجب أن تظهر رسائل تشخيصية شاملة
```

### 2. Database Connection Failed

#### الأسباب المحتملة:
- رابط DATABASE_URL خاطئ
- قاعدة البيانات غير منشأة
- مشكلة في صلاحيات الوصول

#### الحلول:
```bash
# تحقق من صيغة DATABASE_URL
# الصيغة الصحيحة:
postgresql://username:password@hostname:port/database_name

# مثال:
postgresql://taskflow_user:mypassword@dpg-abc123.oregon-postgres.render.com:5432/taskflow_db
```

### 3. Build Failed

#### أسباب محتملة:
- خطأ في requirements.txt
- مشكلة في build.sh
- خطأ في الكود Python

#### حل:
```bash
# تحقق من requirements.txt
pip install -r requirements.txt

# تحقق من build.sh
chmod +x build.sh
./build.sh
```

### 4. Port Already in Use

#### الحل:
```python
# في wsgi.py، تأكد من استخدام المنفذ الصحيح
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

## الملفات المهمة للتشخيص

### 1. wsgi.py
```python
# يحتوي على معلومات تشخيصية شاملة
# يعرض حالة متغيرات البيئة
# يوضح سبب فشل إنشاء التطبيق
```

### 2. config.py
```python
# يحتوي على إعدادات التطبيق
# يعالج تحويل postgres:// إلى postgresql://
# يحدد قيم افتراضية آمنة
```

### 3. build.sh
```bash
# ينفذ المهام التالية:
# - تثبيت الحزم
# - إنشاء قاعدة البيانات
# - تطبيق المايجريشن
```

## أوامر تشخيصية مفيدة

### في البيئة المحلية:
```bash
# اختبار التطبيق
python wsgi.py

# اختبار قاعدة البيانات
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('DB OK')"

# اختبار الاستيراد
python -c "from app import create_app; print('Import OK')"
```

### في Render:
```bash
# فحص السجلات:
# Render Dashboard > Service > Logs

# فحص متغيرات البيئة:
# Render Dashboard > Service > Environment

# إعادة نشر:
# Render Dashboard > Service > Manual Deploy
```

## نصائح للوقاية من المشاكل

### 1. اختبار محلي دائماً:
```bash
# قبل كل push، تأكد من:
python wsgi.py
# يجب أن يعمل بدون أخطاء
```

### 2. استخدام متغيرات بيئة واضحة:
```bash
# في .env.example
SECRET_KEY=example-secret-key
DATABASE_URL=postgresql://user:pass@host:port/db
FLASK_ENV=production
```

### 3. مراقبة السجلات:
- تحقق من سجلات Render بانتظام
- ابحث عن رسائل الخطأ والتحذير
- استخدم رسائل تشخيصية واضحة في الكود

### 4. النسخ الاحتياطية:
```bash
# احفظ نسخة احتياطية من قاعدة البيانات
# استخدم Git tags للإصدارات المستقرة
git tag -a v1.0.0 -m "إصدار مستقر"
git push origin v1.0.0
```

## تواصل للدعم

إذا استمرت المشاكل:
1. تحقق من سجلات Render
2. ارفع issue في GitHub
3. راجع هذا الدليل للحلول الشائعة

---
🚀 **TaskFlow Pro** - نظام إدارة المشاريع المتطور
