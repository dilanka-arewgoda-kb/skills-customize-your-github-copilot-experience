# FastAPI Task Management API - Starter Code
# Install FastAPI and uvicorn first: pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(title="Task Management API", version="1.0.0")

# TODO: Define your Task model using Pydantic BaseModel
# Include fields: id, title, description, completed, created_at


# TODO: Create a list or dictionary to store tasks in memory


# TODO: Implement GET endpoint to retrieve all tasks
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}


# TODO: Implement GET endpoint to retrieve a single task by ID


# TODO: Implement POST endpoint to create a new task


# TODO: Implement PUT endpoint to update an existing task


# TODO: Implement DELETE endpoint to remove a task


# To run this API:
# uvicorn starter-code:app --reload
# Then visit http://localhost:8000/docs to see the interactive documentation
