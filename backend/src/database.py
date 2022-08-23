from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings as _settings


engine = create_engine(_settings.database_url)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine, autocommit = False)
