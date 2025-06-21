#!/bin/bash
# Build script for Render.com

echo "🚀 Starting TaskFlow Pro deployment on Render..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create database tables
echo "🗄️ Setting up database..."
python -c "
from app import create_app, db
app = create_app()
with app.app_context():
    try:
        db.create_all()
        print('✅ Database tables created successfully')
    except Exception as e:
        print(f'⚠️ Database creation error: {e}')
"

echo "✅ Build completed successfully!"
