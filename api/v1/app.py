#!/usr/bin/python3
"""
This module initializes a Flask application and sets up the API.
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS  # Import the CORS class
import os

app = Flask(__name__)

# Register the Blueprint for your views
app.register_blueprint(app_views)

# Create a CORS instance and allow access from all origins (0.0.0.0)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

def close_storage(exception):
    """
    Closes the database storage at the end of the request.
    """
    storage.close()

app.teardown_appcontext(close_storage)

# Define a handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000)

    app.run(host=host, port=port, threaded=True)

