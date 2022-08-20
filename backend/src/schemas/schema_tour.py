from pydantic import BaseModel

from datetime import timedelta

class TourBase(BaseModel):
    name:str 
    min_age:int 
    duration:timedelta 
    number_people: int 

    class Config:
        orm_mode = True