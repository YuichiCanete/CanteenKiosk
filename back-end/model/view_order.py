from fastapi import Depends, APIRouter, Form
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

viewOrderRouter = APIRouter(tags=['View Order'])

@viewOrderRouter.get("/view_order")
async def get_users(db=Depends(get_db)):
    return await fetch_data("view_order",db=db)

@viewOrderRouter.get("/view_order/{order_id}")
async def get_user_by_id(order_id: int,db=Depends(get_db)):
    return await fetch_data("view_order", condition="order_id", value=order_id,db=db)