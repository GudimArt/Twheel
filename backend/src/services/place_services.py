from models.place import Place

from database import Session

class PlaceService():
    async def get_all(self):
        with Session() as session:
            places = session.query(Place).all()
            return places
    async def get_by_id(self, id_):
        with Session() as session:
            place = session.query(Place).filter(Place.id == id_).first()
            return place
    async def add(self, place):
        with Session() as session:
            new_place = Place(**place.dict())
            session.add(new_place)
            session.commit()
    async def delete(self, id_):
        with Session() as session:
            place = session.query(Place).filter(Place.id == id_).first()
            session.delete(place)
            session.commit()
    async def update(self, id_, place):
        with Session() as session:
            session.query(Place).filter(Place.id == id_).update(place.__dict__, synchronize_session = False)
            session.commit()
