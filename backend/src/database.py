from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

from config import settings as _settings


engine = create_engine(_settings.database_url)
Base = declarative_base(engine)

def get_Session():
    Session = sessionmaker(bind=engine)
    return Session
