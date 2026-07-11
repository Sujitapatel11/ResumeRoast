#create  database connection and session management
from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from app.config import settings
#the connection string in a real app, we would use an .evn file. for now we hardcore the docker defualts 
#formats: postgresql:resume_user:resume_pass@localhost:5432/resume_db
#DATABASE_URL = settings.DATABASE_URL
connection_string = settings.DATABASE_URL
#The engine , the enginw is the factory that creates the connection to the database
engine =create_engine(connection_string, echo=settings.DEBUG)
#the dependency, this function yields a session for each requesr abd closes it aferwards 
def get_session() ->Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
#The Initialization, This creates all tables defined in our models
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)