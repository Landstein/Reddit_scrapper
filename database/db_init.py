from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#Absolute Path from the top level project directory
from database.models import Base
#Relative path from the current directory
from database.models import Base
from config import database_config, DATABASE_PATH

#Spins up the database
#engine = create_engine('sqlite:///:database.sql:', echo=False)
config_db = database_config()
directory_path = f'{DATABASE_PATH}/{config_db["database_name"]}'
if int(config_db["in_memory"]):
    engine = create_engine('sqlite://', echo=False)
else:
    engine = create_engine(f"sqlite:///{directory_path}", echo=False)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
session = Session()
