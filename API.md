<div align="center">

![TaskFlow Pro API Documentation](https://placehold.co/1200x300/0d6efd/FFFFFF/png?text=TaskFlow%20Pro%20API%20Documentation)

# 🔌 TaskFlow Pro API Documentation

**Comprehensive RESTful API reference for TaskFlow Pro integration and automation.**

---

<p align="center">
  <img src="https://img.shields.io/badge/API-RESTful-brightgreen?style=for-the-badge" alt="RESTful API">
  <img src="https://img.shields.io/badge/Format-JSON-blue?style=for-the-badge" alt="JSON Format">
  <img src="https://img.shields.io/badge/Auth-Session%20Based-orange?style=for-the-badge" alt="Session Auth">
  <img src="https://img.shields.io/badge/Version-v1.0-purple?style=for-the-badge" alt="Version">
</p>

</div>

---

## 📋 Table of Contents

- [🔐 Authentication](#-authentication)
- [📊 Response Format](#-response-format)
- [🏢 Projects API](#-projects-api)
- [✅ Tasks API](#-tasks-api)
- [👥 Users API](#-users-api)
- [🏛️ Departments API](#-departments-api)
- [⚠️ Risks API](#️-risks-api)
- [📈 Reports API](#-reports-api)
- [❌ Error Handling](#-error-handling)
- [🧪 Testing Examples](#-testing-examples)

---

## 🔐 Authentication

TaskFlow Pro API uses **session-based authentication** with CSRF protection.

### **Login Flow**
```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "user": {
      "id": 1,
      "username": "admin",
      "email": "admin@taskflow.com",
      "role": "admin",
      "department": "Management"
    },
    "csrf_token": "ImY5ZjA4YWY2ZGY4YzQyM2RhN2Q2ZTNkYTUzYjUzYzQyZjFmYzI0NzQi.ZrK5PQ.8H4_q1jNzKY_mNzL4T8QcHJkOvE"
  }
}
```

### **Logout**
```http
POST /api/auth/logout
```

### **Session Validation**
```http
GET /api/auth/me
```

---

## 📊 Response Format

All API responses follow a consistent structure:

```json
{
  "status": "success|error|warning",
  "message": "Human readable message",
  "data": {
    // Response payload
  },
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 100,
    "pages": 10
  },
  "meta": {
    "timestamp": "2025-06-21T10:30:00Z",
    "version": "1.0",
    "request_id": "req_123456789"
  }
}
```

### **HTTP Status Codes**
| Code | Meaning | Description |
|------|---------|-------------|
| `200` | OK | Request successful |
| `201` | Created | Resource created successfully |
| `400` | Bad Request | Invalid request parameters |
| `401` | Unauthorized | Authentication required |
| `403` | Forbidden | Insufficient permissions |
| `404` | Not Found | Resource not found |
| `422` | Unprocessable Entity | Validation errors |
| `500` | Internal Server Error | Server error |

---

## 🏢 Projects API

### **List All Projects**
```http
GET /api/projects
```

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `per_page` (int): Items per page (default: 10)
- `status` (string): Filter by status
- `user_id` (int): Filter by project owner

**Response:**
```json
{
  "status": "success",
  "data": {
    "projects": [
      {
        "id": 1,
        "name": "Website Redesign",
        "description": "Complete redesign of company website",
        "budget": 50000.00,
        "start_date": "2025-01-01T00:00:00Z",
        "end_date": "2025-06-30T00:00:00Z",
        "status": "active",
        "progress": 65,
        "owner": {
          "id": 1,
          "username": "admin",
          "email": "admin@taskflow.com"
        },
        "tasks_count": 15,
        "completed_tasks": 10,
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-06-20T15:30:00Z"
      }
    ]
  },
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 25,
    "pages": 3
  }
}
```

### **Get Specific Project**
```http
GET /api/projects/{id}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "project": {
      "id": 1,
      "name": "Website Redesign",
      "description": "Complete redesign of company website",
      "budget": 50000.00,
      "spent_budget": 32500.00,
      "start_date": "2025-01-01T00:00:00Z",
      "end_date": "2025-06-30T00:00:00Z",
      "status": "active",
      "progress": 65,
      "owner": {
        "id": 1,
        "username": "admin",
        "email": "admin@taskflow.com",
        "department": "Management"
      },
      "tasks": [
        {
          "id": 1,
          "title": "Design Mockups",
          "status": "completed",
          "priority": "high",
          "assigned_to": {
            "id": 2,
            "username": "designer",
            "email": "designer@taskflow.com"
          }
        }
      ],
      "risks": [
        {
          "id": 1,
          "title": "Budget Overrun",
          "severity": "medium",
          "probability": "low",
          "status": "active"
        }
      ]
    }
  }
}
```

### **Create New Project**
```http
POST /api/projects
Content-Type: application/json

{
  "name": "Mobile App Development",
  "description": "Develop iOS and Android mobile applications",
  "budget": 75000.00,
  "start_date": "2025-07-01",
  "end_date": "2025-12-31"
}
```

### **Update Project**
```http
PUT /api/projects/{id}
Content-Type: application/json

{
  "name": "Updated Project Name",
  "budget": 80000.00,
  "status": "on_hold"
}
```

### **Delete Project**
```http
DELETE /api/projects/{id}
```

---

## ✅ Tasks API

### **List Project Tasks**
```http
GET /api/projects/{project_id}/tasks
```

**Query Parameters:**
- `status` (string): Filter by status (pending, in_progress, completed)
- `priority` (string): Filter by priority (low, medium, high)
- `assigned_to` (int): Filter by assigned user ID

### **Create New Task**
```http
POST /api/projects/{project_id}/tasks
Content-Type: application/json

{
  "title": "Create Database Schema",
  "description": "Design and implement database schema for the application",
  "priority": "high",
  "due_date": "2025-07-15",
  "estimated_hours": 8,
  "assigned_to": [2, 3]
}
```

### **Update Task**
```http
PUT /api/tasks/{id}
Content-Type: application/json

{
  "status": "completed",
  "actual_hours": 6,
  "completion_notes": "Task completed successfully with optimizations"
}
```

### **Assign Task to Users**
```http
POST /api/tasks/{id}/assign
Content-Type: application/json

{
  "user_ids": [2, 3, 4],
  "estimated_hours": 8
}
```

---

## 👥 Users API

### **List All Users**
```http
GET /api/users
```

**Query Parameters:**
- `role` (string): Filter by role (admin, manager, user)
- `department_id` (int): Filter by department
- `active` (boolean): Filter active users

### **Get User Profile**
```http
GET /api/users/{id}
```

### **Create New User**
```http
POST /api/users
Content-Type: application/json

{
  "username": "newuser",
  "email": "newuser@taskflow.com",
  "password": "securepassword123",
  "role": "user",
  "department_id": 2
}
```

### **Update User**
```http
PUT /api/users/{id}
Content-Type: application/json

{
  "role": "manager",
  "department_id": 3,
  "active": true
}
```

### **User Activity Statistics**
```http
GET /api/users/{id}/stats
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "user_stats": {
      "total_projects": 5,
      "active_projects": 2,
      "total_tasks": 23,
      "completed_tasks": 18,
      "pending_tasks": 5,
      "total_hours_worked": 156.5,
      "this_month_hours": 32.0,
      "completion_rate": 78.3,
      "avg_task_time": 6.8
    }
  }
}
```

---

## 🏛️ Departments API

### **List All Departments**
```http
GET /api/departments
```

### **Create Department**
```http
POST /api/departments
Content-Type: application/json

{
  "name": "Quality Assurance",
  "description": "Software testing and quality control department"
}
```

### **Department Statistics**
```http
GET /api/departments/{id}/stats
```

---

## ⚠️ Risks API

### **List Project Risks**
```http
GET /api/projects/{project_id}/risks
```

### **Create Risk Assessment**
```http
POST /api/projects/{project_id}/risks
Content-Type: application/json

{
  "title": "Technical Complexity Risk",
  "description": "High technical complexity may lead to delays",
  "severity": "high",
  "probability": "medium",
  "impact": "schedule",
  "mitigation_plan": "Engage senior developers and provide additional training"
}
```

### **Update Risk Status**
```http
PUT /api/risks/{id}
Content-Type: application/json

{
  "status": "mitigated",
  "actual_impact": "minimal",
  "resolution_notes": "Risk successfully managed through proactive measures"
}
```

---

## 📈 Reports API

### **Project Performance Report**
```http
GET /api/reports/projects
```

**Query Parameters:**
- `start_date` (date): Report start date
- `end_date` (date): Report end date
- `format` (string): Response format (json, csv, pdf)

### **User Productivity Report**
```http
GET /api/reports/users/productivity
```

### **Department Workload Report**
```http
GET /api/reports/departments/workload
```

### **Budget Analysis Report**
```http
GET /api/reports/budget-analysis
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "budget_analysis": {
      "total_allocated": 500000.00,
      "total_spent": 324750.00,
      "remaining_budget": 175250.00,
      "utilization_rate": 64.95,
      "projects_over_budget": 2,
      "projects_under_budget": 8,
      "average_budget_variance": -12.3,
      "monthly_burn_rate": 54125.00
    },
    "project_breakdown": [
      {
        "project_id": 1,
        "project_name": "Website Redesign",
        "allocated_budget": 50000.00,
        "spent_budget": 32500.00,
        "remaining_budget": 17500.00,
        "variance_percentage": -35.0
      }
    ]
  }
}
```

---

## ❌ Error Handling

### **Validation Errors**
```json
{
  "status": "error",
  "message": "Validation failed",
  "data": {
    "errors": {
      "email": ["Email address is already registered"],
      "password": ["Password must be at least 8 characters"],
      "budget": ["Budget must be a positive number"]
    }
  }
}
```

### **Authentication Errors**
```json
{
  "status": "error",
  "message": "Authentication required",
  "data": {
    "error_code": "AUTH_REQUIRED",
    "redirect_url": "/login"
  }
}
```

### **Permission Errors**
```json
{
  "status": "error",
  "message": "Insufficient permissions",
  "data": {
    "error_code": "PERMISSION_DENIED",
    "required_role": "manager",
    "current_role": "user"
  }
}
```

---

## 🧪 Testing Examples

### **Using cURL**

```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}' \
  -c cookies.txt

# Get projects (using saved session)
curl -X GET http://localhost:5000/api/projects \
  -b cookies.txt

# Create project
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "name": "API Test Project",
    "description": "Testing project creation via API",
    "budget": 10000.00
  }'
```

### **Using Python Requests**

```python
import requests

# Base URL
BASE_URL = "http://localhost:5000/api"

# Create session
session = requests.Session()

# Login
login_response = session.post(f"{BASE_URL}/auth/login", json={
    "username": "admin",
    "password": "admin123"
})

if login_response.status_code == 200:
    print("✅ Login successful")
    
    # Get projects
    projects_response = session.get(f"{BASE_URL}/projects")
    projects_data = projects_response.json()
    
    print(f"📋 Found {len(projects_data['data']['projects'])} projects")
    
    # Create new project
    new_project = {
        "name": "API Integration Project",
        "description": "Testing API integration capabilities",
        "budget": 25000.00,
        "start_date": "2025-07-01",
        "end_date": "2025-09-30"
    }
    
    create_response = session.post(f"{BASE_URL}/projects", json=new_project)
    
    if create_response.status_code == 201:
        project_data = create_response.json()
        print(f"✅ Project created with ID: {project_data['data']['project']['id']}")
    else:
        print("❌ Failed to create project")
        print(create_response.json())
else:
    print("❌ Login failed")
    print(login_response.json())
```

### **Using JavaScript/Fetch**

```javascript
// Login function
async function login(username, password) {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include', // Important for session cookies
        body: JSON.stringify({ username, password })
    });
    
    return response.json();
}

// Get projects
async function getProjects(page = 1, perPage = 10) {
    const response = await fetch(`/api/projects?page=${page}&per_page=${perPage}`, {
        method: 'GET',
        credentials: 'include'
    });
    
    return response.json();
}

// Create project
async function createProject(projectData) {
    const response = await fetch('/api/projects', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(projectData)
    });
    
    return response.json();
}

// Usage example
(async () => {
    try {
        // Login
        const loginResult = await login('admin', 'admin123');
        if (loginResult.status === 'success') {
            console.log('✅ Login successful');
            
            // Get projects
            const projectsResult = await getProjects();
            console.log('📋 Projects:', projectsResult.data.projects);
            
            // Create new project
            const newProject = {
                name: 'Frontend Revamp',
                description: 'Complete frontend redesign with modern technologies',
                budget: 40000.00
            };
            
            const createResult = await createProject(newProject);
            if (createResult.status === 'success') {
                console.log('✅ Project created:', createResult.data.project);
            }
        }
    } catch (error) {
        console.error('❌ API Error:', error);
    }
})();
```

---

## 🔗 Rate Limiting

TaskFlow Pro API implements rate limiting to ensure fair usage:

- **Authenticated Users**: 1000 requests per hour
- **Unauthenticated Users**: 100 requests per hour
- **Burst Limit**: 20 requests per minute

**Rate Limit Headers:**
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

---

## 🔧 Development & Testing

### **API Testing Tools**
- **Postman Collection**: Available in `/docs/api/postman_collection.json`
- **OpenAPI Spec**: Available at `/api/docs/openapi.json`
- **Swagger UI**: Available at `/api/docs` (development only)

### **Mock Data Generation**
```bash
# Generate test data
python scripts/generate_test_data.py --projects 10 --tasks 50 --users 20
```

---

<div align="center">

### 🚀 Need Help?

**Check out our other documentation:**
- **[Technical Guide](TECHNICAL.md)** - Complete technical documentation
- **[User Guide](docs/user_guide.md)** - End-user manual
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions

---

**TaskFlow Pro API** - Empowering integration and automation for enterprise excellence.

</div>
