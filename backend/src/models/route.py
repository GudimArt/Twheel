from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from database import Base


class Route(Base): 
    __tablename__ ='route'

    def __repr__(self):
        return f'{self.id} {self.name}'
        
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tour_id = Column(Integer, ForeignKey("tour.id"))
    tour = relationship("Tour", back_populates="route", uselist=False)
    places = relationship("Place",  back_populates ='route')
    