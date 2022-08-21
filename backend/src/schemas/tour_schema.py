from pydantic import BaseModel
from typing import Optional

from datetime import timedelta

class TourBase(BaseModel):
    name:str 
    min_age:Optional[int] 
    duration:timedelta 
    number_people: int 
    price: int
    
    class Config:
        orm_mode = True