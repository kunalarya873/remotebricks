from fastapi import APIRouter, HTTPException
from src.app.models.link import LinkID
from src.app.utils.common import get_user_by_email
from src.app.db import db

router = APIRouter()

@router.post("/link-id/")
async def link_id(link_data: LinkID):
    db_user = get_user_by_email(link_data.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")

    db["linked_ids"].insert_one({
        "user_id": str(db_user["_id"]),
        "linked_id": link_data.linked_id
    })
    return {"message": "ID linked successfully."}
