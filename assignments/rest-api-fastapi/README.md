# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You will create a fully functional API with multiple endpoints, request validation, and proper HTTP methods to understand the fundamentals of backend web development.

## 📝 Tasks

### 🛠️	Create a Task Management API

#### Description
Build a REST API for managing tasks using FastAPI. The API should support creating, reading, updating, and deleting tasks (CRUD operations). Each task should have properties like an ID, title, description, completion status, and creation date. You'll implement multiple endpoints that handle different HTTP methods and return proper JSON responses.

#### Requirements
Completed program should:

- Create at least 5 API endpoints: GET all tasks, GET single task by ID, POST to create a task, PUT to update a task, and DELETE to remove a task
- Use FastAPI's Pydantic models to validate request and response data
- Include proper HTTP status codes (200, 201, 404, etc.) for different operations
- Store tasks in memory using a Python list or dictionary (no database required)
- Generate unique IDs for each task automatically
- Handle edge cases like requesting a non-existent task ID (return 404)
- Include proper type hints and documentation that appears in FastAPI's automatic interactive docs


### 🛠️	Test Your API

#### Description
Test your API using FastAPI's built-in interactive documentation (Swagger UI). Verify that all endpoints work correctly and handle various scenarios including error cases.

#### Requirements
Completed testing should:

- Successfully run the API server locally using `uvicorn`
- Access and use the interactive API documentation at `/docs`
- Test all CRUD operations through the Swagger UI interface
- Verify that invalid requests return appropriate error messages
- Demonstrate creating multiple tasks, retrieving them, updating at least one, and deleting at least one
