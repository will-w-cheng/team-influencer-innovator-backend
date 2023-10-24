from datetime import date
import os
import base64
import json
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from __init__ import app, db

# Define the User class for the leaderboard table
class User(db.Model):
    __tablename__ = 'leaderboard'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __init__(self, username, points=0):
        self.username = username
        self.points = points

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        if points >= 0:
            self._points = points

    def create(self):
        """Create a new user entry in the leaderboard table."""
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        """Retrieve user information from the leaderboard table."""
        return {
            "id": self.id,
            "username": self.username,
            "points": self.points
        }

    def update_points(self, points):
        """Update the points of a user in the leaderboard."""
        if points >= 0:
            self.points = points
            db.session.commit()
            return self

    def delete(self):
        """Delete a user from the leaderboard."""
        db.session.delete(self)
        db.session.commit()
        return None

# Function to initialize the leaderboard table with sample data
def initLeaderboard():
    with app.app_context():
        # create the database and the leaderboard table, for now it will just be normal points and whatnot
        db.create_all()
        
        users_data = [
            {"username": "user1", "points": 100},
            {"username": "user2", "points": 150},
            {"username": "user3", "points": 50},
            # Add some more users later for now it's just testing
        ]

        for data in users_data:
            user = User(username=data["username"], points=data["points"])
            user.create()

# Run the initialization function to create and populate the leaderboard
if __name__ == "__main__":
    initLeaderboard()
