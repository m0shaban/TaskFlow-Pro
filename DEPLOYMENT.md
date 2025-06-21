# دليل النشر - TaskFlow Pro

## متطلبات النشر

### الخادم
- Ubuntu 20.04 LTS أو أحدث
- Python 3.8+
- Nginx
- Gunicorn
- SSL Certificate

### قاعدة البيانات
- PostgreSQL (للإنتاج)
- أو MySQL
- أو SQLite (للتطوير فقط)

## خطوات النشر

### 1. إعداد الخادم
```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت Python و pip
sudo apt install python3 python3-pip python3-venv -y

# تثبيت Nginx
sudo apt install nginx -y

# تثبيت PostgreSQL
sudo apt install postgresql postgresql-contrib -y
```

### 2. إعداد قاعدة البيانات
```bash
# إنشاء قاعدة بيانات PostgreSQL
sudo -u postgres psql
CREATE DATABASE taskflow_pro;
CREATE USER taskflow_user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE taskflow_pro TO taskflow_user;
\q
```

### 3. رفع الملفات
```bash
# نسخ المشروع إلى الخادم
git clone <repository_url> /var/www/taskflow-pro
cd /var/www/taskflow-pro

# إعداد البيئة الافتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت الحزم
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### 4. إعداد متغيرات البيئة
```bash
# إنشاء ملف .env
cat > .env << EOF
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://taskflow_user:your_password@localhost/taskflow_pro
FLASK_ENV=production
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
EOF
```

### 5. تهيئة قاعدة البيانات
```bash
# إنشاء الجداول
python db_init.py

# أو استخدام Flask-Migrate
flask db upgrade
```

### 6. إعداد Gunicorn
```bash
# إنشاء ملف خدمة systemd
sudo nano /etc/systemd/system/taskflow-pro.service
```

محتوى الملف:
```ini
[Unit]
Description=TaskFlow Pro
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/taskflow-pro
Environment="PATH=/var/www/taskflow-pro/venv/bin"
ExecStart=/var/www/taskflow-pro/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### 7. إعداد Nginx
```bash
# إنشاء ملف إعداد Nginx
sudo nano /etc/nginx/sites-available/taskflow-pro
```

محتوى الملف:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/taskflow-pro/app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### 8. تفعيل الخدمات
```bash
# تفعيل موقع Nginx
sudo ln -s /etc/nginx/sites-available/taskflow-pro /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# تفعيل خدمة TaskFlow Pro
sudo systemctl enable taskflow-pro
sudo systemctl start taskflow-pro
sudo systemctl status taskflow-pro
```

### 9. إعداد SSL (Let's Encrypt)
```bash
# تثبيت Certbot
sudo apt install certbot python3-certbot-nginx -y

# الحصول على شهادة SSL
sudo certbot --nginx -d your-domain.com
```

## صيانة النظام

### النسخ الاحتياطي
```bash
# نسخ احتياطي لقاعدة البيانات
pg_dump taskflow_pro > backup_$(date +%Y%m%d_%H%M%S).sql

# نسخ احتياطي للملفات
tar -czf taskflow_backup_$(date +%Y%m%d_%H%M%S).tar.gz /var/www/taskflow-pro
```

### المراقبة
```bash
# مراقبة الخدمة
sudo systemctl status taskflow-pro

# مراقبة السجلات
sudo journalctl -u taskflow-pro -f

# مراقبة Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### التحديثات
```bash
# تحديث الكود
cd /var/www/taskflow-pro
git pull origin main

# تحديث الحزم
source venv/bin/activate
pip install -r requirements.txt

# تطبيق ترحيلات قاعدة البيانات
flask db upgrade

# إعادة تشغيل الخدمة
sudo systemctl restart taskflow-pro
```

## الأمان

### إعدادات إضافية
- تفعيل الجدار الناري (UFW)
- إعداد fail2ban
- تشفير قاعدة البيانات
- مراقبة السجلات

### أفضل الممارسات
- تغيير كلمات المرور بانتظام
- تحديث النظام دورياً
- مراقبة استخدام الموارد
- نسخ احتياطية منتظمة

---
**نشر ناجح لـ TaskFlow Pro! 🚀**
