#!/usr/bin/python3
"""
This module defines the API endpoints for managing Place objects.
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage, Place, City, User, Amenity

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    # ... (existing code)

@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    # ... (existing code)

@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    # ... (existing code)

@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    # ... (existing code)

@app_views.route('/places/<place_id>', methods=['PUT'], strictslashes=False)
def update_place(place_id):
    # ... (existing code)

@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """
    Search for Place objects based on JSON request
    """
    json_data = request.get_json()
    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    states = json_data.get('states', [])
    cities = json_data.get('cities', [])
    amenities = json_data.get('amenities', [])

    places = storage.all(Place).values()

    if states:
        places = [place for place in places if place.city.state_id in states]

    if cities:
        places = [place for place in places if place.city_id in cities]

    if amenities:
        places = [place for place in places if all(
            amenity.id in [a.id for a in place.amenities] for amenity in amenities)]

    return jsonify([place.to_dict() for place in places])

