# TaskFlow Pro - دليل النشر على Render

## لماذا Render؟
- ✅ مجاني للمشاريع الصغيرة
- ✅ دعم كامل لـ Flask وPython
- ✅ قاعدة بيانات PostgreSQL مجانية
- ✅ SSL تلقائي
- ✅ سهولة في الإعداد

## 🚨 حل مشكلة gunicorn app:app

### المشكلة:
```
gunicorn.errors.AppImportError: Failed to find attribute 'app' in 'app'.
```

### الحل:
استخدم **wsgi:app** بدلاً من **app:app** في Start Command

## خطوات النشر على Render:

### 1. إنشاء حساب على Render
- اذهب إلى: https://render.com
- سجل دخول بحساب GitHub

### 2. إنشاء Web Service
- اضغط "New" ثم "Web Service"
- اختر مستودع GitHub: m0shaban/TaskFlow-Pro
- اختر Branch: main

### 3. إعدادات الخدمة:
```
Name: taskflow-pro
Environment: Python 3
Root Directory: (اتركه فارغ)
Build Command: pip install -r requirements.txt
Start Command: gunicorn wsgi:app --bind 0.0.0.0:$PORT
```

### 4. متغيرات البيئة:
اذهب إلى Environment واضف:
```
SECRET_KEY=taskflow-pro-secret-key-2025-render
FLASK_ENV=production
DATABASE_URL=(سيتم إضافته تلقائياً عند ربط قاعدة البيانات)
```

### 5. إنشاء قاعدة بيانات PostgreSQL:
- اضغط "New" ثم "PostgreSQL"
- Name: taskflow-pro-db
- Database: taskflow_pro
- User: taskflow_user

### 6. ربط قاعدة البيانات:
- في Web Service اذهب إلى Environment
- اضف متغير DATABASE_URL
- انسخ Internal Database URL من PostgreSQL service

### 7. إعادة النشر:
- اضغط "Manual Deploy" لإعادة النشر
- انتظر حتى يكتمل النشر

## البيانات التجريبية:
بعد النشر الناجح، قم بإنشاء البيانات العينة:
```bash
# في Render Console أو Shell
python setup_sample_data.py
```

## رابط المشروع بعد النشر:
https://taskflow-pro.onrender.com

## مشاكل شائعة وحلولها:

### 1. مشكلة gunicorn app:app
**الحل**: استخدم `gunicorn wsgi:app` في Start Command

### 2. مشكلة قاعدة البيانات
**الحل**: تأكد من إضافة DATABASE_URL في Environment

### 3. مشكلة الصلاحيات
**الحل**: تأكد من أن SECRET_KEY موجود في Environment

### 4. مشكلة البيانات الثابتة
**الحل**: Render يتعامل مع static files تلقائياً
