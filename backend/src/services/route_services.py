from models.route import Route

from database import Session


class RouteService():
    async def get_all(self):
        with Session() as session:
            routes = session.query(Route).all()
            return routes
    async def get_by_id(self, id_):
        with Session() as session:
            route = session.query(Route).filter(Route.id == id_).first()
            return route
    async def add(self, route):
        with Session() as session:
            new_route = Route(**route.dict())
            session.add(new_route)
            session.commit()
    async def delete(self, id_):
        with Session() as session:
            route = session.query(Route).filter(Route.id == id_).first()
            session.delete(route)
            session.commit()
    async def update(self, id_, route):
        with Session() as session:
            session.query(Route).filter(Route.id == id_).update(route.__dict__, synchronize_session = False)
            session.commit()
