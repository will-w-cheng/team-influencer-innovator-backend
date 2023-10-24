import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource  # used for REST API building

from model.users import User

user_api = Blueprint('user_api', __name__,
                     url_prefix='/api/leaderboard')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class LeaderboardAPI:
    class _CRUD(Resource):
        def post(self):
            '''
            Create a new user entry in the leaderboard table.
            Read data from the JSON body.
            '''
            body = request.get_json()

            # Validate username
            username = body.get('username')
            if username is None or len(username) < 2:
                return {'message': f'Username is missing or is less than 2 characters'}, 400

            # Validate points (should be a non-negative integer)
            points = body.get('points')
            if not isinstance(points, int) or points < 0:
                return {'message': 'Points must be a non-negative integer'}, 400

            # Create a new leaderboard entry
            leaderboard_entry = User(username=username, points=points)
            leaderboard_entry.create()

            # Return the newly created leaderboard entry
            return jsonify({'username': leaderboard_entry.username, 'points': leaderboard_entry.points})

        def get(self):
            '''
            Retrieve the leaderboard data.
            Read all leaderboard entries and prepare the output in JSON format.
            '''
            leaderboard_entries = User.query.all()
            leaderboard_data = [{'username': entry.username, 'points': entry.points} for entry in leaderboard_entries]
            return jsonify(leaderboard_data)
        
        def put(self):
            ''' Update user points '''
            body = request.get_json()
            username = body.get('username')
            new_points = body.get('points')

            user = User.query.filter_by(username=username).first()
            if user is None:
                return {'message': 'User not found'}, 404

            if new_points is not None:
                user.update_points(new_points)
                return {'message': f'Updated points for user {user.username}'}



    # Building REST API endpoints
    api.add_resource(_CRUD, '/')  # Create and Read operations
