from models.tour import Tour

from .i_crud import ICrud


class TourService(ICrud):
    async def get_all(self):
        with self.Session() as session:
            try:
                tours = session.query(Tour).all()
            except: 
                raise
            else: 
                return tours
    async def get_by_id(self, id):
        with self.Session() as session:
            try:
                tour = session.query(Tour).filter(Tour.id == id).first()
            except: 
                raise
            else: 
                return tour   
    async def add(self, tour):
        with self.Session() as session:
            try:
                new_tour = Tour(**tour.dict())
                session.add(new_tour)
            except: 
                raise
            else: 
                session.commit()  
    async def delete(self, id):
        with self.Session() as session:
            try:
                tour = session.query(Tour).filter(Tour.id == id).first()
                session.delete(tour)
            except: 
                raise
            else: 
                session.commit()
    async def update(self, tour):
        with self.Session() as session:
            try:
                session.query(Tour).filter(Tour.id == tour.id).update(**tour.dict(), synchronize_session = False)
            except:
                raise
            else:
                session.commit()
