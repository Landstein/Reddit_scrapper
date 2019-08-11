from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#Absolute Path from the top level project directory
from database.models import Base
#Relative path from the current directory
from .models import Base

#Spins up the database
engine = create_engine('sqlite:///:database.sql:', echo=False)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
session = Session()


