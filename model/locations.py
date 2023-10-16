from model.locations import Location  # Import your Location model
from sqlalchemy.exc import IntegrityError

def initLocations():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester records for the table"""
        locations = [
            Location(location_name='Location 1', image='image1.jpg'),
            Location(location_name='Location 2', image='image2.jpg'),
            Location(location_name='Location 3', image='image3.jpg')
        ]

        """Builds sample location data"""
        for location in locations:
            try:
                location.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate location name, or error: {location.location_name}")

if __name__ == "__main__":
    from your_flask_app import app, db  # Import your Flask app and db objects
    initLocations()
