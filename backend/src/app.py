from database import Base

from controllers.tour_controller import router_tour_controller
from controllers.route_controller import router_route_controller
from controllers.place_controller import router_place_controller 

from fastapi import FastAPI
from fastapi import APIRouter


app = FastAPI()
router = APIRouter()

Base.metadata.create_all()

app.include_router(router_tour_controller, tags=["tour_controller"])
app.include_router(router_route_controller, tags=["rout_controller"])
app.include_router(router_place_controller, tags=["place_controller"])


@app.get("/")
async def root():
    return '1'

