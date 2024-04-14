# model/users.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt

router = APIRouter()

# CRUD operations

# GET
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

# POST not working
@router.post("/user/", response_model=dict)
async def create_user(
    user_id: int = Form(...),
    password: str = Form(...), 
    can_tally: bool = Form(...), 
    db=Depends(get_db)
):
    # Hash the password using bcrypt
    hashed_password = hash_password(password)

    query = "INSERT INTO user (user_id, password, can_tally) VALUES (%s, %s, %s)"
    db.execute(query, (user_id, hashed_password, can_tally))  # Pass hashed_password instead of plain text password

    db[0].fetchone()[0]
    db[1].commit()
    return {"user_id": user_id, "password": hashed_password, "can_tally": can_tally}

# PUT

# DELETE

# Hash Password

def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage
