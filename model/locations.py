from __init__ import db
# from flask import render_template  # import render_template from "public" flask libraries
# app = flask(__name__)
class Location(db.Model):

    # Ok so you basically create the new table for the database as the location
    __tablename__ = "locations"

    # Adding the ID field for the table name of locations
    id = db.Column(db.Integer, primary_key=True)

    # Adding the location_name field to the table name of locations in the sqlite db
    location_name = db.Column(db.String, nullable=False)

    # Adding the image tag which will be parse in data as a string which Saaras will input as base64
    image = db.Column(db.String, nullable=False)

    # Class of init location names and images
    def __init__(self, location_name, image):
        self.location_name = location_name
        self.image = image

    # Convert the the db fields into a dictionary where you can access it
    def to_dict(self):
        return {"id": self.id, "location_name": self.location_name, "image": self.image}

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db.session.remove()


def init_locations():
    location1 = Location(location_name="Location 1", image="image1.jpg")
    location2 = Location(location_name="Location 2", image="image2.jpg")
    location3 = Location(location_name="Location 3", image="image3.jpg")

    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)

    db.session.commit()

if __name__ == '__main__':
    # Initialize your database with the application context, so  that it can create it based on the things
    with db.create_scoped_session() as session:
        init_locations()