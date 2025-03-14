#!/usr/bin/python3
"""Create user table"""

import models
from sqlalchemy import Column, String, DateTime
from models.base_model import BaseModel
from sqlalchemy.orm import validates
from datetime import datetime


class User(BaseModel):
    """Class representing a user"""
    __tablename__ = "users"

    name = Column(String(250), nullable=False)
    phone_number = Column(String(20), nullable=False, unique=True)
    pppoe_password = Column(String(50), nullable=False, unique=True)
    location = Column(String(255), nullable=False)
    package = Column(String(60), nullable=False)
    status = Column(String(60), nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)

