from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from datetime import date
from .fn import fetch_data, delete_data, create_data, update_data

router = APIRouter()

@router.get("/users")
async def get_users(db=Depends(get_db)):
    return await fetch_data("user",db=db)

@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int,db=Depends(get_db)):
    return await fetch_data("user", condition="user_id", value=user_id,db=db)

@router.post("/users/", response_model=dict)
async def create_user(
    user_id: int = Form(...),
    password: str = Form(...),
    can_tally: bool = Form(...),
    db=Depends(get_db)
):
    data = {
        "user_id": user_id,
        "password": password,
        "can_tally": can_tally
    }
    return await create_data("user", data, db=db)

@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db=Depends(get_db)):
    return await delete_data("user", "user_id", user_id, db=db)

@router.put("/users/{user_id}", response_model=dict)
async def update_user(
    user_id: int,
    password: str = Form(...),
    can_tally: bool = Form(...),
    db=Depends(get_db)
):
    data = {
        "password": password,
        "can_tally": can_tally
    }
    return await update_data("user", "user_id", user_id, data, db=db)
