### DOWNLOAD psycog2 ###
### DOWNLOAD sqlalchemy ###
### PG ADMIN ###

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# user-name: postgres
# password: admin
# database: sqlalchemy_test
connection_string = 'postgresql+psycopg2://postgres:admin@localhost/sqlalchemy_test'

Base = declarative_base()

engine = create_engine(connection_string, echo=True)  # echo makes the console print all the sql statements being run

def create_all_entities():
    Base.metadata.create_all(engine)

Session = sessionmaker()

local_session = Session(bind=engine)
