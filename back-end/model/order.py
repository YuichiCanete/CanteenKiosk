from fastapi import Depends, APIRouter, Form
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

orderRouter = APIRouter(tags=['Order'])

@orderRouter.get("/order")
async def get_users(db=Depends(get_db)):
    return await fetch_data("`order`",db=db)

@orderRouter.get("/order/{order_id}")
async def get_user_by_id(order_id: int,db=Depends(get_db)):
    return await fetch_data("`order`", condition="order_id", value=order_id,db=db)

@orderRouter.post("/order/", response_model=dict)
async def create_user(
    order_id: int = Form(...),
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "order_id": order_id,
        "user_order_id": user_order_id,
    }
    return await create_data("`order`", data, db=db)

@orderRouter.delete("/order/{order_id}", response_model=dict)
async def delete_user(order_id: int, db=Depends(get_db)):
    return await delete_data("`order`", "order_id", order_id, db=db)

@orderRouter.put("/order/{order_id}", response_model=dict)
async def update_user(
    order_id: int,
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "user_order_id":user_order_id
    }
    return await update_data("`order`", "order_id", order_id, data, db=db)
