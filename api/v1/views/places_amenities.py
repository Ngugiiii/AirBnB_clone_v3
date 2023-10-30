#!/usr/bin/python3
"""
This module defines the routes for the Place-Amenity relationship.
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.app import handle_404


@app_views.route("/places/<place_id>/amenities", methods=["GET"], strict_slashes=False)
def list_amenities(place_id):
    """Retrieve a list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        return handle_404()
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["DELETE"], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """Delete an Amenity object from a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        return handle_404()
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return handle_404()
    if amenity not in place.amenities:
        return handle_404()
    place.amenities.remove(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"], strict_slashes=False)
def link_place_amenity(place_id, amenity_id):
    """Link an Amenity object to a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        return handle_404()
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return handle_404()
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200
    place.amenities.append(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201

