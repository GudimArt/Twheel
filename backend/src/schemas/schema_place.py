from pydantic import BaseModel


class Place(BaseModel):
    name:str
    route_id:int
    image:str 
    availability_cafe:bool
    availability_camp:bool 

    class Config:
        orm_mode = True