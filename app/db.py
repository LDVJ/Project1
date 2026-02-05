from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

DATABSAE_URL = 'postgresql+psycopg2://postgres:ldvj1242210%40L@localhost/project1'

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