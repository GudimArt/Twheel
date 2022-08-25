from typing import Optional, List


from pydantic import BaseModel

from schemas.place_schema import PlaceBase


class RouteBase(BaseModel):
    name:str
    tour_id: Optional[int]

    class Config:
        orm_mode = True
