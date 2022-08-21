from typing import Optional

from pydantic import BaseModel


class Place(BaseModel):
    name:str
    route_id:Optional[int]
    image:str 
    availability_cafe:Optional[bool]
    availability_camp:Optional[bool] 

    class Config:
        orm_mode = True