#!/usr/bin/python3


from models.base_model import Base
from models.db_engine import DBStorage
from models.user import User
from sqlalchemy.orm import sessionmaker
from datetime import datetime

storage = DBStorage()

session = storage._DBStorage__session
# Initialize storage

storage = DBStorage()

Base.metadata.drop_all(storage._DBStorage__engine)
# Create all tables
Base.metadata.create_all(storage._DBStorage__engine)

print("Database tables created successfully!")


user1 = User(
        pppoe_password="user123i",
        name="alice",
        phone_number="070434066",
        status="active",
        payment_date=datetime(2025, 1, 23, 12, 30),
        package="6mbps",
        location="47 past theuri church",
        ip_address="192.168.1.56",
        user_type="static"
        )

user2 = User(
        pppoe_password="user1233",
        name="sammy",
        phone_number="0700545436",
        status="expired",
        payment_date=datetime(2024, 3, 12, 4, 9),
        package="10mbps",
        location="Kasarani oni stage",
        user_type="pppoe"
        )

user3 = User(
        name="winny",
        pppoe_password="user1235",
        phone_number="07434343466",
        status="disconnected",
        payment_date=datetime(2024, 3, 12, 4, 9),
        package="70mbps",
        location="boni stage",
        ip_address="192.168.1.67",
        user_type="static"
        )

session.add_all([user1, user2, user3])
session.commit()

print("users added successfully")

users = session.query(User).all()
for user in users:
    print("***************************************************************")

    print(f"ID: {user.user_id}, Username: {user.name}, pppoe password: {user.pppoe_password}, status: {user.status}, package: {user.package}, payment date: {user.payment_date}, Located at {user.location}")
