# model/users.py
from fastapi import Depends, HTTPException, APIRouter
from .db import get_db

router = APIRouter()

# CRUD operations

@router.get("/user/", response_model=list)
async def read_users(db=Depends(get_db)):
    query = "SELECT user_id, password, can_tally FROM user"
    db.execute(query)
    users = [{"user_id": user[0], "password": user[1], "can_tally":user[2]} for user in db.fetchall()]
    return users

@router.get("/user/{user_id}", response_model=dict)
async def read_user(user_id: int, db=Depends(get_db)):
    query = "SELECT user_id, password, can_tally FROM user WHERE user_id = %s"
    db.execute(query, (user_id,))
    user = db.fetchone()
    if user:
        return {"user_id": user[0], "password": user[1], "can_tally": user[2]}
    raise HTTPException(status_code=404, detail="User not found")
