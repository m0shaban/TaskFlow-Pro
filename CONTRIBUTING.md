<div align="center">

![Contributing to TaskFlow Pro](https://placehold.co/1200x300/0d6efd/FFFFFF/png?text=Contributing%20to%20TaskFlow%20Pro)

# 🤝 Contributing to TaskFlow Pro

**Thank you for your interest in contributing to TaskFlow Pro! This guide will help you get started with contributing to our enterprise-grade project management platform.**

---

<p align="center">
  <a href="#getting-started">🚀 Getting Started</a> •
  <a href="#development-setup">⚙️ Development Setup</a> •
  <a href="#contributing-guidelines">📋 Guidelines</a> •
  <a href="#pull-request-process">🔄 Pull Requests</a> •
  <a href="#code-of-conduct">📜 Code of Conduct</a>
</p>

</div>

---

## 🎯 Ways to Contribute

We welcome contributions in many forms:

| Type | Examples | Difficulty |
|------|----------|------------|
| 🐛 **Bug Reports** | Report issues, crashes, security vulnerabilities | Beginner |
| 💡 **Feature Requests** | Suggest new features, improvements | Beginner |
| 📖 **Documentation** | Improve docs, tutorials, examples | Beginner |
| 🧪 **Testing** | Write tests, improve test coverage | Intermediate |
| 🔧 **Code Contributions** | Bug fixes, new features, optimizations | Intermediate |
| 🏗️ **Architecture** | Design improvements, refactoring | Advanced |
| 🌐 **Translations** | Arabic/English localization | Intermediate |
| 🎨 **UI/UX** | Frontend improvements, design enhancements | Intermediate |

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8 or higher
- Git
- Basic knowledge of Flask and web development
- Familiarity with SQLAlchemy and database concepts

### **First Steps**
1. ⭐ Star the repository
2. 🍴 Fork the repository
3. 📋 Read this contributing guide
4. 🔍 Browse existing issues
5. 💬 Join our community discussions

---

## ⚙️ Development Setup

### **1. Fork & Clone**
```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/TaskFlow-Pro.git
cd TaskFlow-Pro

# Add upstream remote
git remote add upstream https://github.com/m0shaban/TaskFlow-Pro.git
```

### **2. Environment Setup**
```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux  
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### **3. Database Setup**
```bash
# Initialize database
python db_init.py

# Create sample data (optional)
python setup_sample_data.py
```

### **4. Pre-commit Setup**
```bash
# Install pre-commit hooks
pre-commit install

# Test pre-commit (optional)
pre-commit run --all-files
```

### **5. Verify Installation**
```bash
# Run tests
pytest tests/ -v

# Check code quality
black --check app/
flake8 app/
isort --check-only app/

# Start development server
python run.py
```

---

## 📋 Contributing Guidelines

### **🐛 Bug Reports**

#### **Before Submitting**
- [ ] Search existing issues for duplicates
- [ ] Test with the latest version
- [ ] Check if it's already fixed in main branch

#### **Bug Report Template**
```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected Behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
- OS: [e.g. Windows 10, macOS, Ubuntu]
- Python Version: [e.g. 3.11]
- Browser: [e.g. Chrome, Firefox]
- TaskFlow Pro Version: [e.g. 1.0.0]

**Additional Context**
Add any other context about the problem here.
```

### **💡 Feature Requests**

#### **Feature Request Template**
```markdown
**Feature Summary**
A clear and concise description of the feature.

**Problem Statement**
What problem does this feature solve?

**Proposed Solution**
Describe your proposed solution.

**Alternatives Considered**
Describe any alternative solutions you've considered.

**Additional Context**
Add any other context, mockups, or examples.

**Implementation Notes**
Technical considerations or suggestions.
```

### **🔧 Code Contributions**

#### **Code Style Guidelines**
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use type hints where appropriate

#### **Code Quality Standards**
```python
# Good Example
def calculate_project_progress(project_id: int) -> float:
    """Calculate the completion percentage of a project.
    
    Args:
        project_id: The ID of the project to calculate progress for.
        
    Returns:
        The completion percentage as a float between 0.0 and 100.0.
        
    Raises:
        ValueError: If project_id is invalid.
        ProjectNotFoundError: If project doesn't exist.
    """
    project = Project.query.get(project_id)
    if not project:
        raise ProjectNotFoundError(f"Project {project_id} not found")
    
    total_tasks = project.tasks.count()
    if total_tasks == 0:
        return 0.0
        
    completed_tasks = project.tasks.filter_by(status='completed').count()
    return (completed_tasks / total_tasks) * 100.0
```

#### **Testing Requirements**
- Write unit tests for all new functions
- Maintain or improve test coverage
- Test both success and failure scenarios
- Use descriptive test names

```python
# Good Test Example
def test_calculate_project_progress_with_completed_tasks():
    """Test project progress calculation with some completed tasks."""
    # Arrange
    project = create_test_project()
    create_test_task(project, status='completed')
    create_test_task(project, status='pending')
    
    # Act
    progress = calculate_project_progress(project.id)
    
    # Assert
    assert progress == 50.0

def test_calculate_project_progress_with_no_tasks():
    """Test project progress calculation with no tasks."""
    # Arrange
    project = create_test_project()
    
    # Act
    progress = calculate_project_progress(project.id)
    
    # Assert
    assert progress == 0.0
```

---

## 🔄 Pull Request Process

### **1. Branch Strategy**
```bash
# Create feature branch from main
git checkout main
git pull upstream main
git checkout -b feature/amazing-new-feature

# Or for bug fixes
git checkout -b fix/issue-123-login-bug
```

### **2. Development Workflow**
```bash
# Make your changes
# ...edit files...

# Run tests frequently
pytest tests/ -v

# Check code quality
black app/
isort app/
flake8 app/

# Commit with descriptive messages
git add .
git commit -m "✨ Add user dashboard analytics

- Add analytics cards for project overview
- Implement chart.js integration for progress visualization  
- Add responsive design for mobile devices
- Include unit tests for analytics calculations

Fixes #123"
```

### **3. Commit Message Format**
Use conventional commit format with emojis:

```
<type><emoji>: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `✨ feat`: New feature
- `🐛 fix`: Bug fix
- `📚 docs`: Documentation changes
- `🎨 style`: Code style changes (formatting, etc.)
- `♻️ refactor`: Code refactoring
- `🧪 test`: Adding or updating tests
- `⚡ perf`: Performance improvements
- `🔧 chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "✨ feat: Add project risk assessment module

- Implement risk severity calculation algorithm
- Add risk mitigation tracking
- Include email notifications for high-risk projects
- Add comprehensive test suite

Closes #456"

git commit -m "🐛 fix: Resolve user authentication session timeout

- Fix session expiry handling in auth middleware
- Add proper error messages for expired sessions
- Include redirect to login page

Fixes #789"
```

### **4. Pre-Pull Request Checklist**
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No console errors or warnings
- [ ] Commit messages are descriptive
- [ ] Branch is up-to-date with main

### **5. Pull Request Template**
```markdown
## 📋 Description
Brief description of changes made.

## 🎯 Type of Change
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update

## 🧪 Testing
- [ ] Tests pass locally with my changes
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## 📋 Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published

## 📸 Screenshots (if applicable)
Add screenshots to help explain your changes.

## 🔗 Related Issues
Closes #(issue_number)
```

---

## 🧪 Testing Guidelines

### **Test Structure**
```
tests/
├── conftest.py                 # Test configuration
├── test_auth.py               # Authentication tests
├── test_models.py             # Database model tests
├── test_routes.py             # Route functionality tests
├── test_forms.py              # Form validation tests
├── test_api.py                # API endpoint tests
├── integration/               # Integration tests
│   ├── test_user_workflow.py
│   └── test_project_lifecycle.py
└── unit/                      # Unit tests
    ├── test_utils.py
    └── test_services.py
```

### **Writing Good Tests**
```python
# Test class structure
class TestProjectModel:
    """Test suite for Project model."""
    
    def test_create_project_with_valid_data(self, app, db):
        """Test creating project with valid data succeeds."""
        # Arrange
        project_data = {
            'name': 'Test Project',
            'description': 'A test project',
            'budget': 10000.0
        }
        
        # Act
        project = Project(**project_data)
        db.session.add(project)
        db.session.commit()
        
        # Assert
        assert project.id is not None
        assert project.name == 'Test Project'
        assert project.budget == 10000.0
        
    def test_project_progress_calculation(self, app, db, sample_project):
        """Test project progress calculation is accurate."""
        # This test would check the progress calculation logic
        pass
```

### **Running Tests**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_models.py -v

# Run tests matching pattern
pytest -k "test_project" -v

# Run with different verbosity
pytest -v          # verbose
pytest -s          # show print statements
pytest --tb=short  # shorter traceback
```

---

## 📚 Documentation Guidelines

### **Documentation Types**
- **Code Comments**: Explain complex logic
- **Docstrings**: Document all functions and classes
- **README Updates**: Keep installation and usage current
- **API Docs**: Document all endpoints
- **User Guides**: Step-by-step tutorials

### **Docstring Format**
```python
def assign_task_to_user(task_id: int, user_id: int, estimated_hours: float = None) -> TaskAssignment:
    """Assign a task to a user with optional time estimation.
    
    This function creates a new task assignment record and sends
    an email notification to the assigned user.
    
    Args:
        task_id: The ID of the task to assign.
        user_id: The ID of the user to assign the task to.
        estimated_hours: Optional estimated hours for task completion.
        
    Returns:
        TaskAssignment: The created task assignment record.
        
    Raises:
        TaskNotFoundError: If the task doesn't exist.
        UserNotFoundError: If the user doesn't exist.
        DuplicateAssignmentError: If the task is already assigned to the user.
        
    Example:
        >>> assignment = assign_task_to_user(123, 456, 8.0)
        >>> assignment.estimated_hours
        8.0
    """
```

---

## 🌐 Internationalization (i18n)

### **Adding New Translations**
```python
# In templates
{{ _('Welcome to TaskFlow Pro') }}

# In Python code
from flask_babel import gettext as _
flash(_('Project created successfully!'), 'success')
```

### **Translation Workflow**
```bash
# Extract messages
pybabel extract -F babel.cfg -k _l -o messages.pot .

# Update Arabic translations
pybabel update -i messages.pot -d app/translations -l ar

# Compile translations
pybabel compile -d app/translations
```

---

## 🎨 Frontend Guidelines

### **CSS/SASS Structure**
```scss
// Follow BEM methodology
.project-card {
  &__header {
    // Header styles
  }
  
  &__content {
    // Content styles
  }
  
  &--featured {
    // Modifier for featured projects
  }
}
```

### **JavaScript Standards**
```javascript
// Use modern ES6+ features
const fetchProjectData = async (projectId) => {
  try {
    const response = await fetch(`/api/projects/${projectId}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching project data:', error);
    throw error;
  }
};

// Use JSDoc for documentation
/**
 * Updates the project progress bar
 * @param {number} projectId - The project ID
 * @param {number} progress - Progress percentage (0-100)
 */
const updateProgressBar = (projectId, progress) => {
  // Implementation
};
```

---

## 🚨 Security Guidelines

### **Security Checklist**
- [ ] Validate all user inputs
- [ ] Use parameterized queries
- [ ] Implement proper authentication
- [ ] Add CSRF protection
- [ ] Sanitize output
- [ ] Use HTTPS in production
- [ ] Keep dependencies updated

### **Secure Coding Practices**
```python
# Good: Parameterized query
user = User.query.filter_by(username=username).first()

# Bad: String concatenation (SQL injection risk)
# user = db.session.execute(f"SELECT * FROM users WHERE username = '{username}'")

# Good: Input validation
@app.route('/project/<int:project_id>')
def view_project(project_id):
    if project_id <= 0:
        abort(400)
    # ... rest of function

# Good: CSRF protection
class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # CSRF token automatically included
```

---

## 📞 Getting Help

### **Communication Channels**
- **GitHub Issues**: Technical questions and bug reports
- **GitHub Discussions**: General questions and ideas
- **Email**: security@taskflow-pro.com (security issues only)

### **Useful Resources**
- **[Flask Documentation](https://flask.palletsprojects.com/)**
- **[SQLAlchemy Documentation](https://docs.sqlalchemy.org/)**
- **[Bootstrap Documentation](https://getbootstrap.com/docs/)**
- **[Pytest Documentation](https://docs.pytest.org/)**

---

## 📜 Code of Conduct

### **Our Pledge**
We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### **Our Standards**
**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

### **Enforcement**
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at conduct@taskflow-pro.com. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances.

---

## 🏆 Recognition

### **Contributors Hall of Fame**
We recognize and appreciate all contributors to TaskFlow Pro:

#### **Core Team**
- **[Mohamed Shaban](https://github.com/m0shaban)** - Project Lead & Architect

#### **Contributors**
*Your name could be here! Make your first contribution today.*

### **Contribution Rewards**
- **First-time contributors**: Welcome package and recognition
- **Regular contributors**: Special badge and project access
- **Major contributors**: Co-maintainer status consideration
- **Security researchers**: Public acknowledgment and rewards

---

<div align="center">

## 🙏 Thank You!

**Every contribution, no matter how small, helps make TaskFlow Pro better for everyone.**

[![Contributors](https://img.shields.io/github/contributors/m0shaban/TaskFlow-Pro?style=for-the-badge)](https://github.com/m0shaban/TaskFlow-Pro/graphs/contributors)

**Happy Contributing! 🎉**

---

**Questions?** Open an issue or start a discussion. We're here to help! 💪

</div>
