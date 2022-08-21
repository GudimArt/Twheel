from schemas.route_schema import RouteBase

from services.route_services import RouteService

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter


router_route_controller = InferringRouter()


@cbv(router_route_controller)
class RoutController():
    @router_route_controller.get("/routes")
    async def get_all(self):
        return await RouteService.get_all(self)
    @router_route_controller.get("/route/{id}")
    async def get_by_id(self, id:int):
        return await RouteService.get_by_id(self, id)   
    @router_route_controller.post("/route")
    async def add(self, route:RouteBase):
        await RouteService.add(self, route)
    @router_route_controller.delete("/route/{id}")
    async def delete(self, id:int):
        await RouteService.delete(self, id)
    @router_route_controller.put("/route")
    async def update(self, id:int, route:RouteBase):
        await RouteService.update(self, route)