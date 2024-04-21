from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

foodDetailsRouter = APIRouter(tags=['Food Details'])

@foodDetailsRouter.get("/food_details")
async def get_users(db=Depends(get_db)):
    return await fetch_data("food_details",db=db)

@foodDetailsRouter.get("/food_details/{food_detail_id}")
async def get_user_by_id(food_detail_id: int,db=Depends(get_db)):
    return await fetch_data("food_details", condition="food_detail_id", value=food_detail_id,db=db)

@foodDetailsRouter.post("/food_details/", response_model=dict)
async def create_user(
    food_detail_id: int = Form(...),
    name: str = Form(...),
    price: int = Form(...),
    available_stock: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "food_detail_id": food_detail_id,
        "name": name,
        "price": price,
        "available_stock": available_stock
    }
    return await create_data("food_details", data, db=db)

@foodDetailsRouter.delete("/food_details/{food_details_id}", response_model=dict)
async def delete_user(food_details_id: int, db=Depends(get_db)):
    return await delete_data("food_details", "food_detail_id", food_details_id, db=db)

@foodDetailsRouter.put("/food_details/{food_detail_id}", response_model=dict)
async def update_food_detail(
    food_detail_id: int,
    name: str = Form(...),
    price: int = Form(...),
    available_stock: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "name": name,
        "price": price,
        "available_stock": available_stock
    }
    return await update_data("food_details", "food_detail_id", food_detail_id, data, db=db)

