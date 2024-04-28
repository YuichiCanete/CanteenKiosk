from fastapi import Depends, APIRouter, Form, HTTPException
from .db import get_db
import bcrypt
from cryptography.fernet import Fernet
from typing import List

key = b'_7ymBkpL48p4Qq7NLLuaZuhUQfJPKutCvC0y_vKyN7o='
cipher_suite = Fernet(key)

def encrypt_password(password: str) -> str:
    # Encrypt the password using the symmetric key
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8')

def decrypt_password(encrypted_password: str) -> str:
    # Decrypt the password using the symmetric key
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode('utf-8'))
    return decrypted_password.decode('utf-8')

def hash_password(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage

import logging

logger = logging.getLogger(__name__)

async def fetch_data(table_name: str, condition: str = None, value: int = None, db=Depends(get_db)):
    try:
        cursor, _ = db
        query = f"SELECT * FROM {table_name}"
        if condition and value is not None:
            query += f" WHERE {condition} = %s"
            cursor.execute(query, (value,))
        else:
            cursor.execute(query)
        data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        if not data:
            raise HTTPException(status_code=404, detail=f"No data found in {table_name}")
        # Decrypt passwords
        for item in data:
            if "password" in item:
                item["password"] = decrypt_password(item["password"])
        return data
    except Exception as e:
        logger.exception("Error retrieving data")
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")
async def create_data(table_name: str, data: dict, db=Depends(get_db)):
    try:
        cursor, conn = db  # Unpack cursor and connection from the db tuple
        
        # Encrypt password if it exists
        if "password" in data:
            data["password"] = encrypt_password(data["password"])
        
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        # Use the connection object to create the cursor
        cursor.execute(query, tuple(data.values()))
        
        conn.commit()  # Commit changes using the connection object
        cursor.close()
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating data: {str(e)}")


async def delete_data(table_name: str, primary_key: str, primary_value: int, db=Depends(get_db)):
    cursor = None  # Initialize cursor to None
    try:
        cursor, conn = db

        query_check_record = f"SELECT {primary_key} FROM {table_name} WHERE {primary_key} = %s"
        cursor.execute(query_check_record, (primary_value,))
        existing_record = cursor.fetchone()

        if not existing_record:
            raise HTTPException(status_code=404, detail=f"Record with {primary_key}={primary_value} not found")

        # Delete the record
        query_delete_record = f"DELETE FROM {table_name} WHERE {primary_key} = %s"
        cursor.execute(query_delete_record, (primary_value,))
        conn.commit()

        return {"message": f"Record deleted successfully from {table_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        if cursor:  # Check if cursor is not None before closing
            cursor.close()

async def update_data(table_name: str, primary_key: str, primary_value: int, data: dict, db=Depends(get_db)):
    try:
        cursor, conn = db  # Unpack cursor and connection from the db tuple

        # Check if the record exists
        query_check_record = f"SELECT {primary_key} FROM {table_name} WHERE {primary_key} = %s"
        cursor.execute(query_check_record, (primary_value,))
        existing_record = cursor.fetchone()

        if not existing_record:
            raise HTTPException(status_code=404, detail=f"Record with {primary_key}={primary_value} not found")

        # Encrypt password if it exists
        if "password" in data:
            data["password"] = encrypt_password(data["password"])
        
        # Construct the update query dynamically
        set_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query_update_record = f"UPDATE {table_name} SET {set_values} WHERE {primary_key} = %s"
        cursor.execute(query_update_record, tuple(data.values()) + (primary_value,))
        conn.commit()  # Commit changes using the connection object
        cursor.close()

        return {"message": f"Record updated successfully in {table_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

userRouter = APIRouter(tags=['User'])

@userRouter.get("/users")
async def get_users(db=Depends(get_db)):
    return await fetch_data("user",db=db)

@userRouter.get("/users/{user_id}")
async def get_user_by_id(user_id: int,db=Depends(get_db)):
    return await fetch_data("user", condition="user_id", value=user_id,db=db)

@userRouter.post("/users/", response_model=dict)
async def create_user(
    user_id: int = Form(...),
    password: str = Form(...),
    user_type: str = Form(...),
    db=Depends(get_db)
):
    data = {
        "user_id": user_id,
        "password": password,
        "user_type": user_type
    }
    return await create_data("user", data, db=db)

@userRouter.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db=Depends(get_db)):
    return await delete_data("user", "user_id", user_id, db=db)

@userRouter.put("/users/{user_id}", response_model=dict)
async def update_user(
    user_id: int,
    password: str = Form(...),
    user_type: str = Form(...),
    db=Depends(get_db)
):
    data = {
        "password": password,
        "user_type": user_type
    }
    return await update_data("user", "user_id", user_id, data, db=db)
