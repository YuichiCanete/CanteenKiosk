from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.routes import router

app = FastAPI()

# Include CRUD routes from users module
app.include_router(router, prefix="/api")

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
