from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.locations import Location

# Create a Blueprint for the location API
location_api = Blueprint('location_api', __name__, url_prefix='/api/locations')

# Create the API instance
api = Api(location_api)

class LocationAPI(Resource):
    def get(self):
        # Retrieve all locations from the database
        locations = Location.query.all()

        # Prepare the data in JSON format
        json_ready = [location.to_dict() for location in locations]

        # Return the JSON response
        return jsonify(json_ready)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("location_name", required=True, type=str)
        parser.add_argument("image", required=True, type=str)
        args = parser.parse_args()
        location = Location(args["location_name"], args["image"])

        try:
            db.session.add(location)
            db.session.commit()
            return location.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("location_name", type=str)
        parser.add_argument("image", type=str)
        args = parser.parse_args()

        try:
            location = db.session.query(Location).get(args["id"])
            if location:
                if args["location_name"] is not None:
                    location.location_name = args["location_name"]
                if args["image"] is not None:
                    location.image = args["image"]
                db.session.commit()
                return location.to_dict(), 200
            else:
                return {"message": "Location not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            location = db.session.query(Location).get(args["id"])
            if location:
                db.session.delete(location)
                db.session.commit()
                return location.to_dict()
            else:
                return {"message": "Location not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"Error: {exception}"}, 500

# Add the LocationAPI resource to the /api/locations endpoint
api.add_resource(LocationAPI, "/")

class LocationListAPI(Resource):
    def get(self):
        # Retrieve all locations from the database
        locations = Location.query.all()

        # Prepare the data in JSON format
        json_ready = [location.to_dict() for location in locations]

        # Return the JSON response
        return jsonify(json_ready)

# Add the LocationListAPI resource to the /api/locationsList endpoint
api.add_resource(LocationListAPI, "/api/locations")