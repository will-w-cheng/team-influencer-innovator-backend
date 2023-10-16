from __init__ import db

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    def __init__(self, location_name, image):
        self.location_name = location_name
        self.image = image

    def to_dict(self):
        return {"id": self.id, "location_name": self.location_name, "image": self.image}

def init_locations():
    location1 = Location(location_name="Location 1", image="image1.jpg")
    location2 = Location(location_name="Location 2", image="image2.jpg")
    location3 = Location(location_name="Location 3", image="image3.jpg")

    db.session.add(location1)
    db.session.add(location2)
    db.session.add(location3)

    db.session.commit()