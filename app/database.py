from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .core.config import settings #importa as configurações no config do app

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL #pega as configs de db

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
