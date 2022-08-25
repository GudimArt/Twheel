from models.tour import Tour

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from database import get_async_session


class TourService():
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_all(self):
        stmt = select(Tour)
        result = await self.session.execute(stmt)
        tours  = result.scalars().all()
        return tours
    async def get_by_id(self, id_):
        stmt = select(Tour).where(Tour.id == id_)
        result = await self.session.execute(stmt)
        tour  = result.scalars().first()
        return tour
    async def add(self, tour):
        new_tour = Tour(**tour.dict())
        self.session.add(new_tour)
        await self.session.commit()
    async def delete(self, id_):
        stmt = select(Tour).where(Tour.id == id_)
        result = await self.session.execute(stmt)
        tour  = result.scalars().first()
        await self.session.delete(tour)
        await self.session.commit()
    async def update(self, id_, tour):
        stmt = update(Tour).where(Tour.id == id_).values(tour.__dict__)
        await self.session.execute(stmt)
        await self.session.commit()
