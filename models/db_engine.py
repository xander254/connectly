#!/usr/bin/python3
"""Contains Database Engine"""


import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """The class that manages the database"""
    __session = None
    __engine = None

    def __init__(self):
        """Initialize the database"""
        CNTLY_MYSQL_USER = getenv("CNTLY_MYSQL_USER")
        CNTLY_MYSQL_PWD = getenv("CNTLY_MYSQL_PWD")
        CNTLY_MYSQL_HOST = getenv("CNTLY_MYSQL_HOST")
        CNTLY_MYSQL_DB = getenv("CNTLY_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CNTLY_MYSQL_USER,
                                             CNTLY_MYSQL_PWD,
                                             CNTLY_MYSQL_HOST,
                                             CNTLY_MYSQL_DB
                                             ),
                                            pool_pre_ping=True
                                      )

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)


    def new(self, obj):
        """Add a new object to session"""
        self.__session.commit()


    def delete(self):
        """delete an object from session"""
        if obj:
            self.__session.delete(obj)


    def save(self):
        """save all changes to db"""
        self.__session.commit()


    def close(self):
        """Close the session"""
        self.__session.remove()
    
