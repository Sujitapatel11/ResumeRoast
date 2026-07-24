from sqlalchemy.orm import Session, sessionmaker
from app.database.database import engine
#Sessionlocal is a factory that creates a new databases session whenever we call SessionLocal().
SessionLocal = sessionmaker(
    bind = engine, #use the engine we created in database.py
    autoflush = False, #dont automatically flush changes  to the databses
    autocommit = False, #dont automatically commit transactions
)
def get_db():
    """
    create a new database session for each requests, then closes it automatically after the request finishes.
    """
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()