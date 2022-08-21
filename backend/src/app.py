from database import Base

from models.place import Place
from models.route import Route
from models.tour import Tour 

from controllers.tour_controller import router_tour_controller

from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

Base.metadata.create_all()

app.include_router(router_tour_controller, tags=["tour_controller"])

@app.get("/")
async def root():
    return '1'

