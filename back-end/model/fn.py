from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from datetime import date

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
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")


async def create_data(table_name: str, data: dict, db=Depends(get_db)):
    try:
        cursor, conn = db  # Unpack cursor and connection from the db tuple
        
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

        # Construct the update query dynamically
        set_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query_update_record = f"UPDATE {table_name} SET {set_values} WHERE {primary_key} = %s"
        cursor.execute(query_update_record, tuple(data.values()) + (primary_value,))
        conn.commit()  # Commit changes using the connection object
        cursor.close()

        return {"message": f"Record updated successfully in {table_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

