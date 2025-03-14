#!/usr/bin/python3
"""
Base model Other tables will inherit from this model
"""

from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow
                        )

    def save(self):
        """Save the current values to the database"""
        self.updated_at = datetime.utcnow()
        session.add(self)
        session.commit()

    def __str__(self):
        """String rep of object"""
        return f"<{self.__class__.__name__} id={self.id}"

    def delete(self):
        """delete current object from session ans commits"""
        session.delete(self)
        session.commit()

#Base.metadata.create_all(engine)
