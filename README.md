# TaskFlow Pro | تاسك فلو برو
## نظام إدارة المشاريع والمهام المتطور

[![GitHub stars](https://img.shields.io/github/stars/m0shaban/TaskFlow-Pro?style=social)](https://github.com/m0shaban/TaskFlow-Pro)
[![GitHub forks](https://img.shields.io/github/forks/m0shaban/TaskFlow-Pro?style=social)](https://github.com/m0shaban/TaskFlow-Pro)
[![GitHub issues](https://img.shields.io/github/issues/m0shaban/TaskFlow-Pro)](https://github.com/m0shaban/TaskFlow-Pro/issues)
[![License](https://img.shields.io/github/license/m0shaban/TaskFlow-Pro)](https://github.com/m0shaban/TaskFlow-Pro/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)

TaskFlow Pro هو نظام ويب شامل مبني على Flask لإدارة المشاريع والمهام والفرق بطريقة احترافية ومتطورة.

## 🌟 عرض مباشر / Live Demo

🎯 **[جرب التطبيق الآن](https://taskflow-pro.onrender.com)** 

### 🚀 خيارات النشر المتاحة:
- **[Render](https://render.com)** - الأسهل والمُوصى به ⭐
- **[Railway](https://railway.app)** - سريع وبسيط
- **[Heroku](https://heroku.com)** - تقليدي وموثوق
- **[PythonAnywhere](https://pythonanywhere.com)** - للمبتدئين

📋 **دلائل النشر متوفرة:**
- [دليل النشر على Render](RENDER_DEPLOY.md)
- [دليل النشر على Railway](RAILWAY_DEPLOY.md)
- [دليل النشر العام](DEPLOYMENT.md)

## 📸 لقطات شاشة

![TaskFlow Pro Dashboard](https://via.placeholder.com/800x400/0d6efd/ffffff?text=TaskFlow+Pro+Dashboard)
*لوحة التحكم الرئيسية*

![Project Management](https://via.placeholder.com/800x400/198754/ffffff?text=Project+Management)
*إدارة المشاريع*

## 🚀 المميزات الرئيسية

### إدارة المشاريع
- ✅ إنشاء وتعديل وحذف المشاريع
- 📊 تتبع تقدم المشاريع ونسب الإنجاز
- 💰 إدارة الميزانيات والتكاليف
- 📅 تحديد مواعيد البداية والنهاية
- 📎 رفع المرفقات والوثائق

### إدارة المهام
- 📋 إنشاء وتوزيع المهام
- 🎯 تحديد الأولويات (عالية، متوسطة، منخفضة)
- ⏰ تسجيل ساعات العمل والوقت المستغرق
- 👥 تعيين المهام للمستخدمين
- ✅ متابعة حالة إنجاز المهام

### إدارة المستخدمين والصلاحيات
- 👤 نظام مستخدمين متعدد المستويات (مدير، مشرف، مستخدم)
- 🏢 تنظيم المستخدمين حسب الأقسام
- 🔐 نظام مصادقة آمن
- 📧 إدارة البريد الإلكتروني

### إدارة المخاطر والموارد
- ⚠️ تسجيل ومتابعة مخاطر المشاريع
- 🛠️ إدارة الموارد المطلوبة
- 📈 تقارير شاملة عن الأداء

### الواجهة والتقارير
- 🌐 واجهة عربية متجاوبة ومتوافقة مع الهواتف
- 📊 تقارير مفصلة عن المشاريع والأداء
- 📧 إرسال إشعارات عبر البريد الإلكتروني
- 🎨 تصميم عصري باستخدام Bootstrap

## 🛠️ التقنيات المستخدمة

- **Backend**: Python Flask
- **Database**: SQLite مع SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5 RTL
- **JavaScript**: Vanilla JS مع AJAX
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Migrations**: Flask-Migrate
- **Email**: Flask-Mail

## 📋 المتطلبات

- Python 3.8 أو أحدث
- pip (مدير الحزم)
- متصفح ويب حديث

## 🚀 التثبيت والإعداد

### 1. تحميل المشروع
```bash
git clone https://github.com/m0shaban/TaskFlow-Pro.git
cd TaskFlow-Pro
```

### 2. إعداد البيئة الافتراضية
```powershell
# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
.\venv\Scripts\Activate.ps1

# في حالة استخدام Command Prompt
venv\Scripts\activate
```

### 3. تثبيت الحزم المطلوبة### 3. تثبيت الحزم المطلوبة
```powershell
pip install -r requirements.txt
```

### 4. إعداد قاعدة البيانات
```powershell
# إنشاء قاعدة البيانات وجداولها
python db_init.py

# أو استخدام الأمر التالي
python run.py create-tables
```

### 5. إعداد متغيرات البيئة (اختياري)
قم بإنشاء ملف `.env` في جذر المشروع:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## ▶️ تشغيل التطبيق

```powershell
python run.py
```

ثم افتح متصفحك وانتقل إلى: `http://localhost:5000`

## 👤 المستخدم الافتراضي

بعد تهيئة قاعدة البيانات، يمكنك إنشاء بيانات عينة للتجربة:

### إنشاء بيانات عينة (مُوصى به للتجربة)
```powershell
python setup_sample_data.py
```

هذا السكريبت سينشئ:
- **مستخدمين عينة** بصلاحيات مختلفة
- **أقسام تجريبية** (تطوير، تسويق، موارد بشرية، إلخ)
- **مشاريع ومهام عينة** للتجربة

### بيانات تسجيل الدخول العينة:
- **مدير النظام**: `admin` / `admin123`
- **مطور**: `mohammed_dev` / `dev123`
- **مسوق**: `sara_marketing` / `marketing123`

### إنشاء مستخدم مدير يدوياً:
1. التسجيل في النظام كمستخدم عادي
2. تعديل دور المستخدم في قاعدة البيانات إلى `admin`

## 📱 واجهة المستخدم

- **الصفحة الرئيسية**: عرض إحصائيات المشاريع والمهام
- **إدارة المشاريع**: إنشاء وتعديل المشاريع
- **إدارة المهام**: توزيع وتتبع المهام
- **إدارة المستخدمين**: إضافة المستخدمين وتحديد الأدوار
- **التقارير**: تقارير مفصلة عن الأداء

## 📊 الهيكل التنظيمي

```
TaskFlow Pro/
├── app/                    # التطبيق الرئيسي
│   ├── auth/              # نظام المصادقة
│   ├── main/              # الصفحات الرئيسية
│   ├── api/               # API endpoints
│   ├── templates/         # قوالب HTML
│   ├── static/            # الملفات الثابتة
│   └── models.py          # نماذج قاعدة البيانات
├── migrations/            # ملفات ترحيل قاعدة البيانات
├── docs/                  # الوثائق
├── config.py             # إعدادات التطبيق
├── run.py                # نقطة تشغيل التطبيق
└── requirements.txt      # الحزم المطلوبة
```

## 🔧 استكشاف الأخطاء

### مشاكل شائعة وحلولها

**المشكلة**: خطأ في قاعدة البيانات
```powershell
# إعادة تهيئة قاعدة البيانات
python reset_db.py
python db_init.py
```

**المشكلة**: مشاكل في الترحيلات
```powershell
# إصلاح مشاكل الترحيلات
python fix_migrations.py
```

**المشكلة**: مشاكل في قاعدة البيانات
```powershell
# إصلاح قاعدة البيانات
python fix_database.py
```

## 🔐 الأمان

- تشفير كلمات المرور باستخدام Werkzeug
- نظام الجلسات الآمن
- حماية من CSRF
- التحقق من صحة البيانات
- تصفية المدخلات

## 📈 الأداء والتحسين

- استخدام SQLAlchemy ORM للتفاعل مع قاعدة البيانات
- فهرسة الجداول لتحسين الاستعلامات
- التحميل الكسول للعلاقات
- تحسين الاستعلامات للتقارير

## 🤝 المساهمة في المشروع

نرحب بمساهماتكم! اتبعوا الخطوات التالية:

### 1. إنشاء فرع جديد
```bash
git checkout -b feature/اسم-الميزة-الجديدة
```

### 2. تطبيق التغييرات
- اكتب كود نظيف ومنسق
- أضف تعليقات واضحة
- اتبع معايير Python PEP 8

### 3. اختبار التغييرات
```powershell
# تشغيل التطبيق والتأكد من عمله
python run.py
```

### 4. رفع التغييرات
```bash
git add .
git commit -m "إضافة: وصف موجز للتغييرات"
git push origin feature/اسم-الميزة-الجديدة
```

### 5. إنشاء Pull Request
افتح طلب سحب (Pull Request) مع وصف مفصل للتغييرات.

## � الميزات القادمة

- [ ] 📱 تطبيق الهاتف المحمول (React Native)
- [ ] 🔔 إشعارات فورية (WebSocket)
- [ ] 📊 تقارير PDF قابلة للتخصيص
- [ ] 🗓️ تكامل مع التقويم الخارجي (Google Calendar)
- [ ] 💬 نظام الدردشة الداخلي
- [ ] 📍 تتبع GPS للمهام الميدانية
- [ ] 🎨 ثيمات متعددة ووضع داكن
- [ ] 🌍 دعم لغات إضافية
- [ ] 🔗 تكامل مع أدوات خارجية (Slack, Trello)
- [ ] 📈 تحليلات متقدمة للأداء

## �📞 الدعم والمساعدة

- **الوثائق**: راجع مجلد `docs/` للحصول على دلائل مفصلة
- **المشاكل**: أبلغ عن المشاكل في قسم Issues
- **الاقتراحات**: نرحب بآرائكم واقتراحاتكم

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 🙏 شكر وتقدير

- شكر خاص لمجتمع Flask و Python
- Bootstrap لتوفير إطار العمل للواجهة
- جميع المساهمين في تطوير هذا المشروع

---

**TaskFlow Pro | تاسك فلو برو** - نظام إدارة المشاريع الاحترافي
© 2025 - جميع الحقوق محفوظة
# TaskFlow-Pro
