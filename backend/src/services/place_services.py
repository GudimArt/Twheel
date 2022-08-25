from models.place import Place

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from database import get_async_session


class PlaceService():
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_all(self):
        stmt = select(Place)
        result = await self.session.execute(stmt)
        places  = result.scalars().all()
        return places
    async def get_by_id(self, id_):
        stmt = select(Place).where(Place.id == id_)
        result = await self.session.execute(stmt)
        place  = result.scalars().first()
        return place
    async def add(self, place):
        new_place = Place(**place.dict())
        self.session.add(new_place)
        await self.session.commit()
    async def delete(self, id_):
        stmt = select(Place).where(Place.id == id_)
        result = await self.session.execute(stmt)
        place  = result.scalars().first()
        await self.session.delete(place)
        await self.session.commit()
    async def update(self, id_, place):
        stmt = update(Place).where(Place.id == id_).values(place.__dict__)
        await self.session.execute(stmt)
        await self.session.commit()
