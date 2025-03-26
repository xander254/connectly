#!/usr/bin/python
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from flask_restful import Api, Resource
from models.db_engine import DBStorage  # Import your DB manager
from models.user import User  # Import the User model

app = Flask(__name__)
api = Api(app)

# Initialize database storage
storage = DBStorage()
db_session = storage.get_session()  # Get database session


class Users(Resource):
    def get(self, user_id=None):
        """Retrieve users"""
        if user_id:
            user = db_session.query(User).filter_by(id=user_id).first()
            if not user:
                return {"error": "User not found"}, 404
            return user.serialize(), 200
        else:
            users = db_session.query(User).all()
            return [user.serialize() for user in users], 200


api.add_resource(Users, "/users", "/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)

