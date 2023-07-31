from fastapi import FastAPI
from app.controllers.entity_controller import router as entity_router

app = FastAPI()

app.include_router(entity_router)