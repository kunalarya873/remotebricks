from fastapi import FastAPI
from pymongo import MongoClient
from src.app.routers import users, link, join
from fastapi.openapi.utils import get_openapi

# Initialize FastAPI app
app = FastAPI()

# Database Configuration
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string
db = client["user_management"]

# Include Routers
app.include_router(users.router, prefix="/user", tags=["User"])
app.include_router(link.router, prefix="/link", tags=["Link"])
app.include_router(join.router, prefix="/join", tags=["Join"])

# Custom Swagger Documentation
@app.get("/swagger", include_in_schema=False)
def custom_swagger_ui_html():
    return get_openapi(
        title="User Management API",
        version="1.0.0",
        description="APIs for user registration, login, linking IDs, and more.",
        routes=app.routes
    )