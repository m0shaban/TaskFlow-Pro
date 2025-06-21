# دليل المطور - TaskFlow Pro

## هيكل المشروع

```
TaskFlow Pro/
├── app/                          # التطبيق الرئيسي
│   ├── __init__.py              # إعداد التطبيق
│   ├── models.py                # نماذج قاعدة البيانات
│   ├── email.py                 # إرسال الإيميلات
│   ├── tasks.py                 # المهام الخلفية
│   │
│   ├── auth/                    # نظام المصادقة
│   │   ├── __init__.py
│   │   ├── routes.py           # مسارات المصادقة
│   │   └── forms.py            # نماذج المصادقة
│   │
│   ├── main/                    # الصفحات الرئيسية
│   │   ├── __init__.py
│   │   ├── routes.py           # المسارات الرئيسية
│   │   └── forms.py            # النماذج
│   │
│   ├── api/                     # واجهة برمجة التطبيقات
│   │   ├── __init__.py
│   │   └── routes.py           # مسارات API
│   │
│   ├── errors/                  # معالجة الأخطاء
│   │   ├── __init__.py
│   │   └── handlers.py         # معالجات الأخطاء
│   │
│   ├── static/                  # الملفات الثابتة
│   │   └── styles.css          # ملفات CSS مخصصة
│   │
│   └── templates/               # قوالب HTML
│       ├── auth/               # قوالب المصادقة
│       ├── main/               # القوالب الرئيسية
│       ├── docs/               # قوالب التوثيق
│       └── errors/             # قوالب الأخطاء
│
├── migrations/                   # ملفات ترحيل قاعدة البيانات
├── docs/                        # الوثائق
├── instance/                    # ملفات التطبيق المحلية
├── config.py                    # إعدادات التطبيق
├── run.py                       # نقطة تشغيل التطبيق
├── requirements.txt             # الحزم المطلوبة
└── README.md                    # دليل المستخدم
```

## نماذج قاعدة البيانات

### User (المستخدم)
- إدارة المستخدمين والأدوار
- مستويات الصلاحيات: Admin, Manager, User

### Project (المشروع)
- معلومات المشروع والميزانية
- تواريخ البداية والنهاية
- حساب نسبة الإنجاز

### Task (المهمة)
- تفاصيل المهام والأولويات
- تعيين المهام للمستخدمين
- تتبع حالة الإنجاز

### Department (القسم)
- تنظيم المستخدمين حسب الأقسام

### Risk (المخاطر)
- تسجيل مخاطر المشاريع والمهام

### TimeEntry (تسجيل الوقت)
- تتبع ساعات العمل على المهام

## إضافة ميزات جديدة

### 1. إضافة نموذج جديد
```python
# في app/models.py
class NewModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # باقي الحقول...
```

### 2. إنشاء مسار جديد
```python
# في app/main/routes.py
@bp.route('/new-feature')
@login_required
def new_feature():
    return render_template('main/new_feature.html')
```

### 3. إضافة نموذج HTML
```html
<!-- في app/templates/main/new_feature.html -->
{% extends "main/base.html" %}
{% block content %}
<!-- محتوى الصفحة -->
{% endblock %}
```

## إعدادات التطوير

### 1. تفعيل وضع التطوير
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
```

### 2. إنشاء migration جديدة
```bash
flask db migrate -m "description"
flask db upgrade
```

### 3. إضافة بيانات تجريبية
```python
# إنشاء مستخدم مدير
admin = User(username='admin', email='admin@taskflow.com', role=UserRole.ADMIN)
admin.set_password('admin123')
db.session.add(admin)
db.session.commit()
```

## أفضل الممارسات

### 1. الكود
- اتبع معايير PEP 8
- أضف تعليقات واضحة
- استخدم أسماء متغيرات وصفية

### 2. قاعدة البيانات
- استخدم المفاتيح الخارجية للعلاقات
- أضف فهارس للحقول المستخدمة في البحث
- استخدم القيود المناسبة

### 3. الأمان
- تحقق من صحة البيانات
- استخدم CSRF protection
- شفّر كلمات المرور

### 4. الواجهة
- استخدم Bootstrap للتصميم المتجاوب
- أضف رسائل التنبيه المناسبة
- تأكد من دعم RTL للعربية

## اختبار التطبيق

### تشغيل الاختبارات
```bash
# تشغيل التطبيق في وضع التطوير
python run.py

# فتح المتصفح
http://localhost:5000
```

### بيانات اختبار
- المستخدم: admin
- كلمة المرور: admin123

## استكشاف الأخطاء

### مشاكل شائعة
1. **خطأ في قاعدة البيانات**: `python reset_db.py`
2. **مشاكل في الترحيلات**: `python fix_migrations.py`
3. **أخطاء في الصلاحيات**: تحقق من الأدوار في User model

## التحديثات المستقبلية

### ميزات مقترحة
- [ ] إشعارات فورية
- [ ] تطبيق الهاتف المحمول
- [ ] تصدير التقارير PDF
- [ ] تكامل مع التقويم الخارجي
- [ ] نظام الدردشة الداخلي
- [ ] تتبع GPS للمهام الميدانية

---
**TaskFlow Pro** - تم التطوير بكل حب واهتمام 💻❤️
