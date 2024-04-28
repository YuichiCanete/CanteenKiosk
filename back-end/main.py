from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.user import userRouter
from model.food_details import foodDetailsRouter
from model.user_order import userOrderRouter
from model.food import foodRouter
from model.order import orderRouter
from model.tally import tallyRouter
from model.view_order import viewOrderRouter

app = FastAPI()

# Include CRUD routes from users module
app.include_router(userRouter, prefix="/api")
app.include_router(foodDetailsRouter, prefix="/api")
app.include_router(userOrderRouter, prefix="/api")
app.include_router(foodRouter, prefix="/api")
app.include_router(orderRouter, prefix="/api")
app.include_router(tallyRouter, prefix="/api")
app.include_router(viewOrderRouter, prefix="/api")


# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
