from fastapi import Depends, HTTPException, APIRouter, Form
from datetime import date
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

userOrderRouter = APIRouter(tags=['User Order'])

@userOrderRouter.get("/user_order")
async def get_users(db=Depends(get_db)):
    return await fetch_data("user_order",db=db)

@userOrderRouter.get("/user_order/{user_order_id}")
async def get_user_by_id(user_order_id: int,db=Depends(get_db)):
    return await fetch_data("user_order", condition="user_order_id", value=user_order_id,db=db)

@userOrderRouter.post("/user_order/", response_model=dict)
async def create_user(
    user_order_id: int = Form(...),
    payment_type: str = Form(...),
    order_date: date = Form(...),
    total_price: int = Form(...),
    user_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "user_order_id": user_order_id,
        "payment_type": payment_type,
        "order_date": order_date,
        "total_price": total_price,
        "user_id": user_id
    }
    return await create_data("user_order", data, db=db)

@userOrderRouter.delete("/user_order/{user_order}", response_model=dict)
async def delete_user(user_order_id: int, db=Depends(get_db)):
    return await delete_data("user_order", "user_order_id", user_order_id, db=db)

@userOrderRouter.put("/user_order/{user_order_id}", response_model=dict)
async def update_food_detail(
    user_order_id: int,
    payment_type: str = Form(...),
    order_date: date = Form(...),
    total_price: int = Form(...),
    user_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "payment_type": payment_type,
        "order_date": order_date,
        "total_price": total_price,
        "user_id": user_id
    }
    return await update_data("user_order", "user_order_id", user_order_id, data, db=db)

