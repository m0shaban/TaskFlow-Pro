<div align="center">

![TaskFlow Pro Banner](https://placehold.co/1200x400/0d6efd/FFFFFF/png?text=TaskFlow%20Pro)

# 🏛️ Project TaskFlow: The Strategic Execution & Governance Platform

<<<<<<< HEAD
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

## 🧪 أدوات التشخيص والاختبار

### اختبار شامل للنظام
```powershell
# اختبار اتصال قاعدة البيانات وإنشاء التطبيق
python test_database.py
```

### فحص متغيرات البيئة
```powershell
# اختبار WSGI والمتغيرات البيئية
python wsgi.py
```

### أدوات التشخيص للمشاكل الشائعة:

**1. مشكلة Internal Server Error:**
- راجع ملف `TROUBLESHOOTING.md` للحلول المفصلة
- تأكد من ضبط `SECRET_KEY` و `DATABASE_URL`

**2. مشاكل قاعدة البيانات:**
```powershell
# اختبار الاتصال فقط
python -c "from test_database import test_database_connection; test_database_connection()"
```

**3. فحص صحة التطبيق:**
```powershell
# اختبار Flask app
python -c "from test_database import test_flask_app; test_flask_app()"
```

**4. إعدادات النشر:**
- راجع ملفات `DEPLOYMENT.md` و `RENDER_DEPLOY.md`
- تأكد من وجود جميع الملفات المطلوبة: `Procfile`, `wsgi.py`, `build.sh`

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
=======
**A comprehensive, enterprise-grade web application designed to align strategic goals with daily operations, providing total transparency and control over projects, tasks, and resources.**
>>>>>>> 3a7ab370c0f2e192ee81b2db6a7b9c3aec127e47

---

### 🚀 **[View the Live Application Here](https://taskflow-pro-hkcv.onrender.com)** 🚀

---

<p align="center">
  <a href="https://github.com/m0shaban/TaskFlow-Pro/stargazers"><img src="https://img.shields.io/github/stars/m0shaban/TaskFlow-Pro?style=for-the-badge&logo=github&color=gold" alt="Stars"></a>
  <a href="https://github.com/m0shaban/TaskFlow-Pro/network/members"><img src="https://img.shields.io/github/forks/m0shaban/TaskFlow-Pro?style=for-the-badge&logo=github&color=blueviolet" alt="Forks"></a>
  <a href="https://github.com/m0shaban/TaskFlow-Pro/issues"><img src="https://img.shields.io/github/issues/m0shaban/TaskFlow-Pro?style=for-the-badge&logo=github&color=red" alt="Issues"></a>
</p>

</div>

### 🎯 The Strategic Challenge

In large organizations and government bodies, there is often a critical disconnect between high-level strategy and day-to-day execution. Teams work in silos, management lacks a clear, real-time view of project progress and risks, and accountability becomes diluted. This lack of a "single source of truth" leads to inefficiency, wasted resources, and the ultimate failure to achieve key strategic objectives.

---

### 💡 The Architectural Solution

TaskFlow Pro is architected to be a centralized **"Enterprise Operating System."** It creates a transparent, hierarchical flow of information from the highest strategic level down to individual tasks. The architecture ensures that every action is aligned, measurable, and visible.

1.  **Centralized Data Core:** A robust relational database (powered by SQLAlchemy ORM) serves as the single source of truth for all projects, tasks, resources, and risks, eliminating data silos.
2.  **Role-Based Access Control (RBAC):** A sophisticated user management system ensures that every user—from administrator to team member—has access to exactly the information and functionality they need, guaranteeing security and focus.
3.  **Integrated Reporting & Notification Engine:** An automated system provides stakeholders at all levels with real-time dashboards, detailed performance reports, and email notifications, ensuring that crucial information reaches the right people at the right time.

> This platform moves organizations from fragmented operations to unified, strategic execution.

---

### ✨ Key Features & Functionality

| Category | Feature | Icon |
| :--- | :--- | :---: |
| **Strategic Portfolio Management** | Create & manage complex projects with detailed budgets, timelines, and risk assessments. | 📂 |
| **Tactical Task Execution** | Assign tasks, set priorities, track man-hours, and monitor progress in real-time. | ✅ |
| **Resource & Team Governance** | Manage users by department, assign roles & permissions, and track resource allocation. | 👥 |
| **Risk Mitigation** | A dedicated module for identifying, tracking, and mitigating project risks before they escalate. | ⚠️ |
| **Executive-Level Reporting** | Generate comprehensive, data-driven reports on project performance, team productivity, and financial status. | 📊 |

---

### ⚙️ Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white)

---

### 🖼️ Visual Demo

*(A dynamic GIF showcasing the fluid user experience is essential. It should quickly cycle through: 1. The main dashboard with its key stats. 2. The project list view. 3. A detailed view of a single project with its tasks. 4. An example of a generated report.)*

<div align="center">

![Animation of the TaskFlow Pro application showing dashboards, project management, and reporting features.](https://placehold.co/800x450/0d6efd/FFFFFF/gif?text=Live%20Application%20Demo)

</div>

---

### 🚀 Potential for National & Enterprise Scale

TaskFlow Pro is not just a tool; it's a governance framework ready for immediate, large-scale deployment.

#### **Enterprise Application**
This is a turnkey "Enterprise Operating System" that can be deployed across an entire corporation. It enables complete operational transparency, allowing C-suite executives to monitor the performance of every department and ensure that all activities are directly aligned with the company's strategic objectives.

#### **National & Governmental Application**
This platform is perfectly suited for government ministries to manage their internal operations, execute national initiatives, and track departmental performance. It provides a robust framework for project governance, efficient resource allocation, risk mitigation, and public accountability—all of which are essential for the effective functioning of the public sector and the successful implementation of national development plans like Egypt's Vision 2030.
