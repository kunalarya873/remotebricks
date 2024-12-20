from fastapi import FastAPI
from pymongo import MongoClient
from src.app.routers import users, link, join

# Initialize FastAPI app
app = FastAPI()

# Database Configuration
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string
db = client["user_management"]

# Include Routers
app.include_router(users.router, prefix="/user", tags=["User"])
app.include_router(link.router, prefix="/link", tags=["Link"])
app.include_router(join.router, prefix="/join", tags=["Join"])

# app/main.py
