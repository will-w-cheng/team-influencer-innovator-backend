import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.users import User

locations_api = Blueprint('location_api', __name__, url_prefix='/api/locations')
api = Api(locations_api)


class LocationAPI:
    class _CRUD(Resource):
        def post(self):
            ''' Create a new location and place '''
            body = request.get_json()
            location_name = body.get('location_name')
            image = body.get('image')

            # Validate location_name and image fields
            if location_name is None or len(location_name) < 2:
                return {'message': 'Location name is missing or too short'}, 400

            if image is None:
                return {'message': 'Image is missing'}, 400

            # Create a new location record
            new_location = Location(location_name=location_name, image=image)
            location = new_location.create()

            if location:
                return jsonify(location.read())
            else:
                return {'message': 'Error creating location'}, 400

        def get(self):
            ''' Retrieve a list of all locations and places '''
            locations = Location.query.all()
            json_ready = [location.read() for location in locations]
            return jsonify(json_ready)
        
        
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name)

    # Register the locations API blueprint
    app.register_blueprint(locations_api)

    # Run the Flask app
    app.run(debug=True)