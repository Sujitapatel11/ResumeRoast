"""
Base class for all SQLAlchemy models.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class inherited by every database model.
    """

    pass