#!/usr/bin/python3
"""
Initialization of app_views Blueprint.
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views import amenities, cities, index, places, states, users, places_reviews, places_amenities
