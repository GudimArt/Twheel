from schemas.place_schema import PlaceBase

from services.place_services import PlaceService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from fastapi import Depends

router_place_controller = InferringRouter()


@cbv(router_place_controller)
class PlaceController():
    def __init__(self, place_services: PlaceService = Depends(PlaceService)):
        self.place_services = place_services

    @router_place_controller.get("/places")
    async def get_all(self):
        return await self.place_services.get_all()

    @router_place_controller.get("/place/{id}")
    async def get_by_id(self, id_:int):
        return await self.place_services.get_by_id(id_)

    @router_place_controller.post("/place")
    async def add(self, place:PlaceBase):
        await self.place_services.add(place)

    @router_place_controller.delete("/place/{id}")
    async def delete(self, id_:int):
        await self.place_services.delete(id_)

    @router_place_controller.put("/place")
    async def update(self, id_:int, place:PlaceBase):
        await self.place_services.update(id_, place)
