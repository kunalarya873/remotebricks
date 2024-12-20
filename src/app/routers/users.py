from fastapi import APIRouter, HTTPException
from src.app.models.users import UserRegistration, UserLogin
from src.app.utils.hashing import hash_password, verify_password
from src.app.utils.common import get_user_by_email
from src.app.db import db

router = APIRouter()

@router.post("/register/")
async def register_user(user: UserRegistration):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")

    hashed_password = hash_password(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password
    }
    db["users"].insert_one(user_data)
    return {"message": "User registered successfully."}

@router.post("/login/")
async def login_user(user: UserLogin):
    db_user = get_user_by_email(user.email)
    print(db_user.get('joined_date'))
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"message": "Login successful."}
