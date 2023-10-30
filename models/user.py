#!/usr/bin/python3
""" holds class User"""
import hashlib
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    """
    User class
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        password = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a User instance.
        """
        super().__init__(*args, **kwargs)
        if getenv("HBNB_TYPE_STORAGE") == "db":
            if 'password' in kwargs:
                self.password = hashlib.md5(kwargs['password'].encode()).hexdigest()

