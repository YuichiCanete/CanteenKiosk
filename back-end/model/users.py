# model/users.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from datetime import date
import bcrypt

router = APIRouter()

# CRUD operations

# GET
@router.get("/user/{user}", response_model=list)
async def read_users(db=Depends(get_db)):
    query = "SELECT user_id, password, can_tally FROM user"
    db.execute(query)
    users = [{"user_id": user[0], "password": user[1], "can_tally":user[2]} for user in db.fetchall()]
    return users

@router.get("/food/{food}", response_model=list)
async def read_food(food: int, db=Depends(get_db)):
    query = "SELECT food_id, quantity, order_id, food_detail_id FROM food where food_id=%s"
    db.execute(query)
    
    users = [{"food_id": user[0], "quantity": user[1], "order_id":user[2], "food_detail_id":user[3]} for user in db.fetchall()]
    return users

@router.get("/food_details/{food_details}", response_model=list)
async def read_food_details(food_details: int, db=Depends(get_db)):
    query = "SELECT food_detail_id, name, price, available_stock FROM food_detail"
    db.execute(query)
    users = [{"food_detail_id": user[0], "name": user[1], "price":user[2], "available_stock":user[3]} for user in db.fetchall()]
    return users

@router.get("/order/{order}", response_model=list)
async def read_order(order: int, db=Depends(get_db)):
    query = "SELECT order_id, user_order_id FROM order"
    db.execute(query)
    users = [{"order_id": user[0], "user_order_id": user[1]} for user in db.fetchall()]
    return users

@router.get("/tally/{tally}", response_model=list)
async def read_tally(tally: int, db=Depends(get_db)):
    query = "SELECT tally_id, tally_status, salary_period, user_order_id FROM tally"
    db.execute(query)
    users = [{"tally_id": user[0], "tally_status": user[1], "salary_period":user[2], "user_order_id":user[3]} for user in db.fetchall()]
    return users

@router.get("/user_order/{user_order}", response_model=list)
async def read_user_order(user_order: int, db=Depends(get_db)):
    query = "SELECT user_order_id, payment_type, order_date, total_price, user_id FROM user_order"
    db.execute(query)
    users = [{"user_order_id": user[0], "payment_type": user[1], "order_date": user[2], "total_price":user[3], "user_id":user[4]} for user in db.fetchall()]
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

@router.post("/food/", response_model=dict)
async def create_user(
    food_id: int = Form(...),
    quantity: int = Form(...), 
    order_id: int = Form(...),
    food_detail_id: int = Form(...), 
    db=Depends(get_db)
):
    
    query = "INSERT INTO user (food_id, quantity, order_id, food_detail_id) VALUES (%s, %s, %s, %s)"
    db.execute(query, (food_id, quantity, order_id, food_detail_id)) 

    db[0].fetchone()[0]
    db[1].commit()
    return {"food_id": food_id, "quantity": quantity, "order_id": order_id, "food_detail_id": food_detail_id}

@router.post("/food_details/", response_model=dict)
async def create_user(
    food_detail_id: int = Form(...),
    name: str = Form(...), 
    price: int = Form(...),
    available_stock: int = Form(...), 
    db=Depends(get_db)
):
    
    query = "INSERT INTO user (food_detail_id, name, price, available_stock) VALUES (%s, %s, %s, %s)"
    db.execute(query, (food_detail_id, name, price, available_stock)) 

    db[0].fetchone()[0]
    db[1].commit()
    return {"food_detail_id": food_detail_id, "name": name, "price": price, "available_stock": available_stock}

@router.post("/order/", response_model=dict)
async def create_user(
    order_id: int = Form(...),
    user_order_id: int = Form(...),  
    db=Depends(get_db)
):
    
    query = "INSERT INTO user (order_id, user_order_id) VALUES (%s, %s)"
    db.execute(query, (order_id, user_order_id)) 

    db[0].fetchone()[0]
    db[1].commit()
    return {"order_id": order_id, "user_order_id": user_order_id}

@router.post("/tally/", response_model=dict)
async def create_user(
    tally_id: int = Form(...),
    tally_status: str = Form(...), 
    salary_period: date = Form(...),
    user_order_id: int = Form(...), 
    db=Depends(get_db)
):
    
    query = "INSERT INTO user (tally_id, tally_status, salary_period, user_order_id) VALUES (%s, %s, %s, %s)"
    db.execute(query, (tally_id, tally_status, salary_period, user_order_id)) 

    db[0].fetchone()[0]
    db[1].commit()
    return {"tally_id": tally_id, "tally_status": tally_status, "salary_period": salary_period, "user_order_id": user_order_id}

@router.post("/user_order/", response_model=dict)
async def create_user(
    user_order_id: int = Form(...),
    payment_type: str = Form(...), 
    order_date: date = Form(...),
    total_price: int = Form(...),
    user_id: int = Form(...), 
    db=Depends(get_db)
):
    
    query = "INSERT INTO user (user_order_id, payment_type, order_date, total_price, user_id) VALUES (%s, %s, %s, %s, %s)"
    db.execute(query, (user_order_id, payment_type, order_date, total_price, user_id)) 

    db[0].fetchone()[0]
    db[1].commit()
    return {"user_order_id": user_order_id, "payment_type": payment_type, "order_date": order_date, "total_price": total_price, "user_id": user_id}

# PUT
@router.put("/user/{user_id}", response_model=dict)
async def update_user(
    user_id: int,
    password: str = Form(...),
    can_tally: str = Form(...),
    db=Depends(get_db)
):
    # Update user information in the database 
    query = "UPDATE users SET password = %s, can_tally = %s WHERE user_id = %s"
    db[0].execute(query, (password, can_tally))
    db[1].commit()
    return {"user_id": user_id, "password":password, "can_tally": can_tally}
    
    # If no rows were affected, user not found
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/food/{food_id}", response_model=dict)
async def update_user(
    food_id: int,
    quantity: int = Form(...), 
    order_id: int = Form(...),
    food_detail_id: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE users SET quantity = %s, order_id = %s, food_detail_id = %s WHERE food_id = %s"
    db[0].execute(query, (quantity, order_id, food_detail_id))
    db[1].commit()
    return {"food_id": food_id, "quantity": quantity, "order_id": order_id, "food_detail_id": food_detail_id}
    
    raise HTTPException(status_code=404, detail="Food not found")

@router.put("/food_details/{food_detail_id}", response_model=dict)
async def update_user(
    food_detail_id: int,
    name: str = Form(...), 
    price: int = Form(...),
    available_stock: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE users SET name = %s, price = %s, available_stock = %s WHERE food_detail_id = %s"
    db[0].execute(query, (name, price, available_stock))
    db[1].commit()
    return {"food_detail_id": food_detail_id, "name": name, "price": price, "available_stock": available_stock}
    
    raise HTTPException(status_code=404, detail="Food Details not found")
 
@router.put("/order/{order_id}", response_model=dict)
async def update_user(
    order_id: int,
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE users SET user_order_id = %s WHERE order_id = %s"
    db[0].execute(query, (user_order_id))
    db[1].commit()
    return {"order_id": order_id, "user_order_id": user_order_id}
    
    raise HTTPException(status_code=404, detail="Order not found")

@router.put("/tally/{tally_id}", response_model=dict)
async def update_user(
    tally_id: int,
    tally_status: str = Form(...), 
    salary_period: date = Form(...),
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE users SET tally_status = %s, salary_period = %s, user_order_id = %s WHERE tally_id = %s"
    db[0].execute(query, (tally_status, salary_period, user_order_id))
    db[1].commit()
    return {"tally_id": tally_id, "tally_status": tally_status, "salary_period": salary_period, "user_order_id": user_order_id}
    
    raise HTTPException(status_code=404, detail="Tally not found")
 
@router.put("/user_order/{user_order_id}", response_model=dict)
async def update_user(
    user_order_id: int,
    payment_type: str = Form(...), 
    order_date: date = Form(...),
    total_price: int = Form(...),
    user_id: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE users SET payment_type = %s, order_date = %s, total_price = %s , user_id = %s WHERE user_order_id = %s"
    db[0].execute(query, (payment_type, order_date, total_price, user_id))
    db[1].commit()
    return {"user_order_id": user_order_id, "payment_type": payment_type, "order_date": order_date, "total_price": total_price, "user_id": user_id}
    
    raise HTTPException(status_code=404, detail="User Order not found")
 
# DELETE
@router.delete("/user/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT user_id FROM user WHERE user_id = %s"
        db[0].execute(query_check_user, (user_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM user WHERE user_id = %s"
        db[0].execute(query_delete_user, (user_id,))
        db[1].commit()

        return {"message": "User deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
 
@router.delete("/food/{food_id}", response_model=dict)
async def delete_user(
    food_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT food_id FROM food WHERE food_id = %s"
        db[0].execute(query_check_user, (food_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM food WHERE food_id = %s"
        db[0].execute(query_delete_user, (food_id,))
        db[1].commit()

        return {"message": "Food deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
  
@router.delete("/food_details/{food_details_id}", response_model=dict)
async def delete_user(
    food_details_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT food_details_id FROM food_details WHERE food_details_id = %s"
        db[0].execute(query_check_user, (food_details_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="Food Details not found")

        # Delete the user
        query_delete_user = "DELETE FROM food_details WHERE food_details_id = %s"
        db[0].execute(query_delete_user, (food_details_id,))
        db[1].commit()

        return {"message": "Food Details deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
  
@router.delete("/order/{order_id}", response_model=dict)
async def delete_user(
    order_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT order_id FROM order WHERE order_id = %s"
        db[0].execute(query_check_user, (order_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM order WHERE order_id = %s"
        db[0].execute(query_delete_user, (order_id,))
        db[1].commit()

        return {"message": "Order deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
  
@router.delete("/tally/{tally_id}", response_model=dict)
async def delete_user(
    tally_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT tally_id FROM tally WHERE tally_id = %s"
        db[0].execute(query_check_user, (tally_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM tally WHERE tally_id = %s"
        db[0].execute(query_delete_user, (tally_id,))
        db[1].commit()

        return {"message": "Tally deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
  
@router.delete("/user_order/{user_order_id}", response_model=dict)
async def delete_user(
    user_order_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT user_order_id FROM user_order WHERE user_order_id = %s"
        db[0].execute(query_check_user, (user_order_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise HTTPException(status_code=404, detail="User Order not found")

        # Delete the user
        query_delete_user = "DELETE FROM user_order WHERE user_order_id = %s"
        db[0].execute(query_delete_user, (user_order_id,))
        db[1].commit()

        return {"message": "User Order deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
 
# Hash Password

def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage
