from flask import Flask
from flask_cors import CORS
from .routes import configure_routes

def create_app():
    app = Flask(__name__)

    # LIBERA a origem do frontend (http://localhost:5173)
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    configure_routes(app)
    return app