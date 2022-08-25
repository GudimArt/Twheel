
from schemas.route_schema import RouteBase

from services.route_services import RouteService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from fastapi import Depends

router_route_controller = InferringRouter()


@cbv(router_route_controller)
class RoutController():
    def __init__(self, route_services: RouteService = Depends(RouteService)):
        self.route_services = route_services

    @router_route_controller.get("/routes")
    async def get_all(self):
        return await self.route_services.get_all()

    @router_route_controller.get("/route/{id}")
    async def get_by_id(self, id_:int):
        return await self.route_services.get_by_id(id_)

    @router_route_controller.post("/route")
    async def add(self, route:RouteBase):
        await self.route_services.add(route)

    @router_route_controller.delete("/route/{id}")
    async def delete(self, id_:int):
        await self.route_services.delete(id_)

    @router_route_controller.put("/route")
    async def update(self, id_:int, route:RouteBase):
        await self.route_services.update(id_, route)
