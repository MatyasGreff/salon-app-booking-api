from flask import Flask
from flask_cors import CORS

from src.exception import GlobalException
from src.routes import register_routes      #Importing modules


def create_app():
    app = Flask(__name__)
    # route
    register_routes(app)                    
    GlobalException.handle(app)             # Error handlers
    CORS(app, resources={r"/*": {"origins": "*"}})  #This bit allows cross origin requests
    return app