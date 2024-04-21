from fastapi import Depends, APIRouter, Form
from datetime import date
from .db import get_db
from .fn import fetch_data, delete_data, create_data, update_data

tallyRouter = APIRouter(tags=['Tally'])

@tallyRouter.get("/tally")
async def get_users(db=Depends(get_db)):
    return await fetch_data("tally",db=db)

@tallyRouter.get("/tally/{tally_id}")
async def get_user_by_id(tally_id: int,db=Depends(get_db)):
    return await fetch_data("tally", condition="tally_id", value=tally_id,db=db)

@tallyRouter.post("/tally/", response_model=dict)
async def create_user(
    tally_id: int = Form(...),
    tally_status: str = Form(...),
    salary_period: date = Form(...),
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "tally_id": tally_id,
        "tally_status": tally_status,
        "salary_period": salary_period,
        "user_order_id": user_order_id
    }
    return await create_data("tally", data, db=db)

@tallyRouter.delete("/tally/{tally_id}", response_model=dict)
async def delete_user(tally_id: int, db=Depends(get_db)):
    return await delete_data("tally", "tally_id", tally_id, db=db)

@tallyRouter.put("/tally/{tally_id}", response_model=dict)
async def update_food_detail(
    tally_id: int,
    tally_status: str = Form(...),
    salary_period: date = Form(...),
    user_order_id: int = Form(...),
    db=Depends(get_db)
):
    data = {
        "tally_status": tally_status,
        "salary_period": salary_period,
        "user_order_id": user_order_id
    }
    return await update_data("tally", "tally_id", tally_id, data, db=db)