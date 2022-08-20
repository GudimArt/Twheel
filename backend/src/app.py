from database import Base

from models.place import Place
from models.route import Route
from models.tour import Tour 

from services.crud.crud_tour import router_crud_tour

from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

Base.metadata.create_all()

app.include_router(router_crud_tour, tags=["tour"])

@app.get("/")
async def root():
    return '1'

