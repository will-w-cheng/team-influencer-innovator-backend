from __init__ import db
import base64
import os

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
image_path = "static/assets/images/"  # Relative path to the image
# locationposition=(20, 45)
# AND locationposition=(20, 45)
def init_locations():
    # Initialize data for now just from lists but later we push it into a database
    b64_lst = []
    '''
    If you want to add an image you can just put it in the static/assets/images
    But also append your coordinates to the following list below 
    '''
    coordinates_data = ["250, 500", "100, 450"]


    '''
    Now from here what we do is we loop through all the filenames and the image_path and then append them to lists so it's easy to just loop through later
    and then add them to a session
    '''
    count = 0
    filenames = [filename for filename in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, filename))]

    # Sort the filenames alphabetically
    sorted_filenames = sorted(filenames)
    for filename in sorted_filenames:
        if os.path.isfile(os.path.join(image_path, filename)):
            count += 1
            b64_lst.append(image_to_base64(image_path + filename))


    #### Add stuff to the db now
    for b64_image in range(0, len(b64_lst)):
        location = Location(location_name=coordinates_data[b64_image], image=b64_lst[b64_image])
        db.session.add(location)
        db.session.commit()

    

    '''
    Old code for this location 
    '''


    # location1 = Location(location_name="20, 45", image=base64_data)
    # location2 = Location(location_name="35, 40", image=base64_data2)
    # # location3 = Location(location_name="Location 3", image="image3.jpg")  # Placeholder for the third image

    # db.session.add(location1)
    # db.session.add(location2)
    # # db.session.add(location3)

    # db.session.commit()

if __name__ == '__main__':
    init_locations()
