# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)  # Enable CORS for all routes
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app