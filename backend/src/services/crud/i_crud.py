from abc import ABCMeta, abstractmethod

from database import get_Session
from fastapi import APIRouter, Depends


class ICrud ():
    __metaclass__ = ABCMeta
    
    Session = get_Session()

    @abstractmethod
    async def get_all():
        pass
    @abstractmethod
    async def get_by_id():
        pass
    @abstractmethod
    async def add():
        pass
    @abstractmethod
    async def delete():
        pass
    @abstractmethod
    async def update():
        pass