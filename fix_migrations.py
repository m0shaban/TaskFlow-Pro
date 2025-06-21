from flask_migrate import current, merge_heads
from app import create_app, db
import subprocess
import os
import sys

def run_command(command):
    """Run a shell command and print the output."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result

def fix_migrations():
    """Fix migration issues by merging the heads."""
    app = create_app()
    with app.app_context():
        # Step 1: Check the current migration heads
        print("Checking migration heads...")
        heads_result = run_command("flask db heads")
        
        # Step 2: Merge the heads
        print("\nMerging migration heads...")
        merge_result = run_command("flask db merge heads")
        
        # Step 3: Apply the migrations
        print("\nApplying migrations...")
        upgrade_result = run_command("flask db upgrade")
        
        # Step 4: Create a new migration
        print("\nCreating a new migration for your changes...")
        migrate_result = run_command('flask db migrate -m "Merged migrations and added new features"')
        
        # Step 5: Apply the new migration
        print("\nApplying the new migration...")
        final_upgrade = run_command("flask db upgrade")
        
        print("\n=== Migration Fix Completed ===")
        print("If you're still experiencing issues, you might need to manually edit the migration files.")
        print("Check the migrations directory and ensure the dependencies are correct.")

if __name__ == "__main__":
    fix_migrations()
