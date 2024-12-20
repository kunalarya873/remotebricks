from fastapi import APIRouter, HTTPException
from src.app.utils.common import get_user_by_email
from src.app.db import db
from bson import ObjectId
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

router = APIRouter()


def convert_object_id(data):
    """
    Recursively convert ObjectId to string in a dictionary or list.
    """
    if isinstance(data, dict):
        return {key: convert_object_id(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_object_id(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data

@router.get("/joined-data/{email}/")
async def get_joined_data(email: str):
    db_user = get_user_by_email(email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    # Log user data for debugging
    logger.info(f"Fetched user: {db_user}")

    linked_ids = list(db["linked_ids"].find({"user_id": str(db_user["_id"])}))
    
    user_data = convert_object_id({
        "username": db_user["username"],
        "email": db_user["email"],
        "joined_date": db_user.get("joined_date", datetime.now()),  # This is where the field is checked
        "_id": db_user["_id"]
    })
    linked_ids = convert_object_id(linked_ids)

    return {
        "user": user_data,
        "linked_ids": linked_ids
    }
@router.delete("/delete-user/{email}/")
async def delete_user(email: str):
    db_user = get_user_by_email(email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    db["users"].delete_one({"_id": db_user["_id"]})
    db["linked_ids"].delete_many({"user_id": str(db_user["_id"])})
    return {"message": "User and associated data deleted successfully."}
