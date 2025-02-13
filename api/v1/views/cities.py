#!/usr/bin/python3
"""
This module defines the API endpoints for managing City objects.
"""
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage, City, State

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """
    Retrieves the list of all City objects of a State.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """
    Retrieves a City object by ID.
    """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """
    Deletes a City object by ID.
    """
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({})
    else:
        abort(404)

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """
    Creates a new City object.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')

    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()
    return jsonify(new_city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """
    Updates a City object by ID.
    """
    city = storage.get(City, city_id)
    if city:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
        for key, value in data.items():
            if key not in ['id', 'state_id', 'created_at', 'updated_at']:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict())
    else:
        abort(404)

