from schemas.place_schema import PlaceBase

from services.place_services import PlaceService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter


router_place_controller = InferringRouter()


@cbv(router_place_controller)
class PlaceController():
    @router_place_controller.get("/places")
    async def get_all(self):
        return await PlaceService.get_all(self)

    @router_place_controller.get("/place/{id}")
    async def get_by_id(self, id_:int):
        return await PlaceService.get_by_id(self, id_)

    @router_place_controller.post("/place")
    async def add(self, place:PlaceBase):
        await PlaceService.add(self, place)

    @router_place_controller.delete("/place/{id}")
    async def delete(self, id_:int):
        await PlaceService.delete(self, id_)

    @router_place_controller.put("/place")
    async def update(self, id_:int, place:PlaceBase):
        await PlaceService.update(self, id_, place)
        