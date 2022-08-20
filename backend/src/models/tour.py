from sqlalchemy import Column, Integer, String, Interval
from sqlalchemy.orm import relationship, backref

from database import Base


class Tour(Base):
    __tablename__ = 'tour'
    
    def __repr__(self):
        return f'{self.id} {self.name}'
        
    id = Column(Integer, primary_key=True)
    name = Column(String)
    min_age = Column(Integer)
    duration = Column(Interval)
    number_people = Column(Integer)
    route = relationship("Route", back_populates="tour", uselist=False)
    