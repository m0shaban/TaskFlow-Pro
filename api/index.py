from app import create_app

# إنشاء التطبيق
app = create_app()

# للنشر على Vercel
if __name__ == "__main__":
    app.run(debug=False)
