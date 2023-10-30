from __init__ import db
import base64

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

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()
        base64_encoded = base64.b64encode(image_binary)
        base64_string = base64_encoded.decode("utf-8")
        return base64_string

# Example usage
image_path = "static/assets/IMG_0902.jpg"  # Relative path to the image
base64_data = image_to_base64(image_path)
image_path2 = "static/assets/IMG_0908.jpg"  # Another relative path to a different image
base64_data2 = image_to_base64(image_path2)
# locationposition=(20, 45)
# AND locationposition=(20, 45)
def init_locations():
    location1 = Location(location_name="176, 450", image=base64_data)
    location2 = Location(location_name="35, 40", image=base64_data2)
    #location3 = Location(location_name="Location 3", image="image3.jpg")  # Placeholder for the third image

    db.session.add(location1)
    db.session.add(location2)
    # db.session.add(location3)

    db.session.commit()

if __name__ == '__main__':
    init_locations()
