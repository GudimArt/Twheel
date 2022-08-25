from models.route import Route

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from database import get_async_session

class RouteService():
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_all(self):
        stmt = select(Route)
        result = await self.session.execute(stmt)
        routes  = result.scalars().all()
        return routes
    async def get_by_id(self, id_):
        stmt = select(Route).where(Route.id == id_)
        result = await self.session.execute(stmt)
        route  = result.scalars().first()
        return route
    async def add(self, route):
        new_route = Route(**route.dict())
        self.session.add(new_route)
        await self.session.commit()
    async def delete(self, id_):
        stmt = select(Route).where(Route.id == id_)
        result = await self.session.execute(stmt)
        route  = result.scalars().first()
        await self.session.delete(route)
        await self.session.commit()
    async def update(self, id_, route):
        stmt = update(Route).where(Route.id == id_).values(route.__dict__)
        await self.session.execute(stmt)
        await self.session.commit()
