from models.tour import Tour
from schemas.schema_tour import TourBase

from .i_crud import ICrud

from fastapi import APIRouter

router = APIRouter()

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter


router_crud_tour = InferringRouter()

@cbv(router_crud_tour)
class CrudTour(ICrud):

    @router_crud_tour.get("/tours")
    async def get_all(self):
        with self.Session() as session:
            try:
                tours = session.query(Tour).all()
            except:
                raise
            finally:
                return tours
    @router_crud_tour.get("/tour/{id}")
    async def get_by_id(self, id:int):
        with self.Session() as session:
            try:
                tour = session.query(Tour).filter(Tour.id == id).first()
            except:
                raise
            finally:
                return tour   
    @router_crud_tour.post("/tour")
    async def add(self, tour:TourBase):
        with self.Session() as session:
            try:
                new_tour = Tour(**tour.dict())
                session.add(new_tour)
            except:
                raise
            finally:
                session.commit()  
    @router_crud_tour.delete("/tours/{id}")
    async def delete(self, id:int):
        with self.Session() as session:
            try:
                tour = session.query(Tour).filter(Tour.id == id).first()
                session.delete(tour)
            except:
                raise
            finally:
                session.commit()
    @router_crud_tour.put("/tour")
    async def update(self):
        pass
