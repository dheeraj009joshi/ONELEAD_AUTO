# app/__init__.py
from flask import Flask
from app.Route.User_route import user_bp
from app.Route.generat_route import general_bp
def create_app():
    app = Flask(__name__)
    app.secret_key = 'Dheeraj@2006'
    app.register_blueprint(user_bp)
    app.register_blueprint(general_bp)
    # Other app configuration and setup here
    return app