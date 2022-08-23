from schemas.tour_schema import TourBase

from services.tour_services import TourService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter


router_tour_controller = InferringRouter()


@cbv(router_tour_controller)
class TourController():
    @router_tour_controller.get("/tours")
    async def get_all(self):
        return await TourService.get_all(self)

    @router_tour_controller.get("/tour/{id}")
    async def get_by_id(self, id_:int):
        return await TourService.get_by_id(self, id_)

    @router_tour_controller.post("/tour")
    async def add(self, tour:TourBase):
        await TourService.add(self, tour)

    @router_tour_controller.delete("/tour/{id}")
    async def delete(self, id_:int):
        await TourService.delete(self, id_)

    @router_tour_controller.put("/tour")
    async def update(self, id_:int, tour:TourBase):
        await TourService.update(self, id_, tour)
