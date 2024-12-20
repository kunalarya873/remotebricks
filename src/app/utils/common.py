from bson.objectid import ObjectId
from src.app.db import db

def get_user_by_email(email: str):
    return db["users"].find_one({"email": email})