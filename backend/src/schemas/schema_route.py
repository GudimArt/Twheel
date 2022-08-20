from typing import List


from pydantic import BaseModel

from schema_place import PlaceBase


class RouteBase(BaseModel):
    name:str 
    tour_id:int 
    places: List[PlaceBase]

    class Config:
        orm_mode = True