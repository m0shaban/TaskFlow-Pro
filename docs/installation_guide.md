# دليل تثبيت وإعداد نظام إدارة المشاريع

![شعار النظام](https://cdn-icons-png.flaticon.com/512/7486/7486754.png)

**مطور النظام: المهندس محمد شعبان**
**البريد الإلكتروني: eng.mohamed0shaban@gmail.com**
**الهاتف: 201121891913+**

## المتطلبات

### متطلبات النظام:
- Python 3.9 أو أحدث
- قاعدة بيانات SQLite (افتراضي) أو MySQL أو PostgreSQL
- 2GB RAM (الحد الأدنى)
- 1GB مساحة تخزين حرة

### المكتبات والإعتماديات:
- Flask 2.3.2
- Flask-Login 0.6.2
- Flask-SQLAlchemy 3.0.5
- Flask-Migrate 4.0.4
- Flask-WTF 1.1.1
- وغيرها من المكتبات المذكورة في ملف requirements.txt

## خطوات التثبيت

### 1. إعداد بيئة Python الافتراضية
```bash
# إنشاء مجلد المشروع (إذا لم يكن موجوداً)
mkdir project_management_system
cd project_management_system

# إنشاء بيئة Python افتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# لنظام Windows
venv\Scripts\activate
# لنظام Linux/Mac
source venv/bin/activate
```

### 2. استنساخ المشروع وتثبيت المكتبات المطلوبة
```bash
# استنساخ المشروع من GitHub (إذا كان متاحاً)
git clone <رابط المستودع>

# أو قم بنسخ ملفات المشروع إلى المجلد

# تثبيت المكتبات المطلوبة
pip install -r requirements.txt
```

### 3. تكوين المشروع

1. انسخ ملف `.env.example` إلى ملف `.env` جديد:
```bash
cp .env.example .env
```

2. قم بتعديل ملف `.env` بالإعدادات المناسبة:
