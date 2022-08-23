from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Place(Base):
    __tablename__ ='place'

    def __repr__(self):
        return f'{self.id} {self.name}'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    route_id = Column(Integer, ForeignKey("route.id"))
    route = relationship("Route", back_populates="places", uselist=False)
    image = Column(String, nullable=False)
    availability_cafe = Column(Boolean)
    availability_camp = Column(Boolean)
