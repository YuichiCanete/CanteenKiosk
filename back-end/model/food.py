from fastapi import Depends, APIRouter, Form
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

foodRouter = APIRouter(tags=['Food'])

@foodRouter.get("/food")
async def get_users(db=Depends(get_db)):
    return await fetch_data("food",db=db)

@foodRouter.get("/food/{food_id}")
async def get_user_by_id(food_id: int,db=Depends(get_db)):
    return await fetch_data("food", condition="food_id", value=food_id,db=db)

@foodRouter.post("/food/", response_model=dict)
async def create_user(
    food_id: int = Form(...),
    quantity: int = Form(...),
    order_id: int = Form(...),
    food_detail_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "food_id": food_id,
        "quantity": quantity,
        "order_id": order_id,
        "food_detail_id": food_detail_id
    }
    return await create_data("food", data, db=db)

@foodRouter.delete("/food/{food_id}", response_model=dict)
async def delete_user(food_id: int, db=Depends(get_db)):
    return await delete_data("food", "food_id", food_id, db=db)

@foodRouter.put("/food/{food_id}", response_model=dict)
async def update_food_detail(
    food_id: int,
    quantity: int = Form(...),
    order_id: int = Form(...),
    food_detail_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "quantity": quantity,
        "order_id": order_id,
        "food_detail_id": food_detail_id
    }
    return await update_data("food", "food_id", food_id, data, db=db)