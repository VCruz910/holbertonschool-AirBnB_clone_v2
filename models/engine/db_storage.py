#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        __engine = create_engine(
            f"mysql+mysqldb://{usr}:{pwd}@{host}/{db}", pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in
            storage by class or in general"""
        query_dict = {}
        if cls is None:
            for v in classes.values():
                for obj in self.__session.query(v):
                    k = obj.__class__.__name__ + '.' + obj.id
                    query_dict[k] = obj
        elif cls in classes:
            for obj in self.__session.query(classes[cls]):
                k = obj.__class__.__name__ + '.' + obj.id
                query_dict[k] = obj
            return query_dict

    def new(self, obj):
        """Add object"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
