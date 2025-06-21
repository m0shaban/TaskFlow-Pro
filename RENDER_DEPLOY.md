# TaskFlow Pro - دليل النشر على Render

## لماذا Render؟
- ✅ مجاني للمشاريع الصغيرة
- ✅ دعم كامل لـ Flask وPython
- ✅ قاعدة بيانات PostgreSQL مجانية
- ✅ SSL تلقائي
- ✅ سهولة في الإعداد

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
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app
```

### 4. متغيرات البيئة:
```
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://...  (سيتم إنشاؤها تلقائياً)
FLASK_ENV=production
```

### 5. إنشاء قاعدة بيانات PostgreSQL:
- اضغط "New" ثم "PostgreSQL"
- Name: taskflow-pro-db
- انسخ رابط قاعدة البيانات إلى DATABASE_URL

## رابط المشروع بعد النشر:
https://taskflow-pro.onrender.com
