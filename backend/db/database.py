#Here we're going to define the database initialization so that we can then create the database models in the models folder.

from sqlalchemy import create_engine #This is the function that will create the engine that wraps around the database we're going to interact with
from sqlalchemy.orm import sessionmaker #This is the function that will create the session that will be used to interact with the database
from sqlalchemy.ext.declarative import declarative_base #This is the function that will create the base class that will be used to create the database models.

from core.config import settings

engine = create_engine(settings.DATABASE_URL) #This is the engine that will be used to interact with the database, which we point to by the DATABASE_URL in the .env file

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #This is the session that will be used to interact with the database, which we bind to the engine we created above

Base = declarative_base() #This is the base class that will be used to create the database models, which we inherit from the declarative_base function we imported above

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine) #This will create the tables in the database according to the models we have defined in the models folder
