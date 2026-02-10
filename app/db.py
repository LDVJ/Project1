from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
from .config import settings


DATABSAE_URL = f'postgresql+psycopg2://{settings.DB_USERNAME}:{quote_plus(settings.DB_PASSWORD)}@{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(DATABSAE_URL)

sessionLocal = sessionmaker(
                    autocommit=False,
                    autoflush=False,
                    bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        print("DB connected Successfully")
        yield db
    finally:
        print('DB Disconnected')
        db.close()