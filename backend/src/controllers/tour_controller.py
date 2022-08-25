from schemas.tour_schema import TourBase

from services.tour_services import TourService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from database import get_async_session


router_tour_controller = InferringRouter()


@cbv(router_tour_controller)
class TourController():
    def __init__(self, tour_services: TourService = Depends(TourService)):
        self.tour_services = tour_services

    @router_tour_controller.get("/tours")
    async def get_all(self):
        return await self.tour_services.get_all()

    @router_tour_controller.get("/tour/{id}")
    async def get_by_id(self, id_:int):
        return await self.tour_services.get_by_id(id_)

    @router_tour_controller.post("/tour")
    async def add(self, tour:TourBase):
        await self.tour_services.add(tour)

    @router_tour_controller.delete("/tour/{id}")
    async def delete(self, id_:int):
        await self.tour_services.delete(id_)

    @router_tour_controller.put("/tour")
    async def update(self, id_:int, tour:TourBase):
        await self.tour_services.update(id_, tour)
        