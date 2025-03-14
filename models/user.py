#!/usr/bin/python3
"""Create user table"""

import models
from sqlalchemy import Column, String, DateTime
from models.base_model import BaseModel
from sqlalchemy.orm import validates
from datetime import datetime


class User(BaseModel, Base):
    """Class representing a user"""
    __tablename__ = "users"

    user_id = Column(Integer, nullable=False, Primary_key=True)
    mikrotik_id = Column(String(15), nullable=True)
    name = Column(String(250), nullable=False)
    phone_number = Column(String(20), nullable=False, unique=True)
    pppoe_password = Column(String(50), nullable=False, unique=True)
    location = Column(String(255), nullable=False)
    package = Column(String(60), nullable=False)
    status = Column(String(60), nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    user_type = Column(Enum("static", "pppoe"), nullable=False)
    ip_address = Column(string(15),nullable=True)


    def to_dict(self):
        """
        Converts user object to dictionary making it 
        serializable for api

        This representation is not dry...after implementing v0 api it has to be changed in base model
        """
        return {
                "user_id" = self.user_id,
                "mikrotik_id" = self.mikrotik_id,
                "name" = self.name,
                "phone_number" = self.phone_number,
                "pppoe_password" = self.pppoe_password,
                "location" = self.location,
                "package" = self.package,
                "status" = self.status,
                "payment_date" = self.payment_date,
                "user_type" = self.user_type,
                "ip_address" = self.ip_address
                }

