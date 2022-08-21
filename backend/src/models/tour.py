from sqlalchemy import Column, Integer, String, Interval
from sqlalchemy.orm import relationship, backref

from database import Base


class Tour(Base):
    __tablename__ = 'tour'
    
    def __repr__(self):
        return f'{self.id} {self.name}'
        
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    min_age = Column(Integer)
    duration = Column(Interval, nullable=False)
    number_people = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    route = relationship("Route", back_populates="tour", uselist=False)
    