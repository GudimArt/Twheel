from models.tour import Tour

from database import Session


class TourService():
    async def get_all(self):
        with Session() as session:
            tours = session.query(Tour).all()
            return tours
    async def get_by_id(self, id_):
        with Session() as session:
            tour = session.query(Tour).filter(Tour.id == id_).first()
            return tour
    async def add(self, tour):
        with Session() as session:
            new_tour = Tour(**tour.dict())
            session.add(new_tour)
            session.commit()
    async def delete(self, id_):
        with Session() as session:
            tour = session.query(Tour).filter(Tour.id == id_).first()
            session.delete(tour)
            session.commit()
    async def update(self, id_, tour):
        with Session() as session:
            session.query(Tour).filter(Tour.id == id_).update(tour.__dict__)
            session.commit()
