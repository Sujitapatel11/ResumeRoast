from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text
from app.core.config import settings

def get_engine():
    try:
        engine = create_engine(
            settings.DATABASE_URL,
            echo=False,
            pool_pre_ping=True,
        )
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine
    except Exception:
        # Fallback to SQLite when PostgreSQL is offline
        connect_args = {"check_same_thread": False}
        return create_engine(
            settings.SQLITE_URL,
            echo=False,
            connect_args=connect_args
        )

engine = get_engine()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session