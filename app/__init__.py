from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from dotenv import load_dotenv
from .routes import register_blueprints

load_dotenv() 

# Initialize the database and migration engine
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    
    register_blueprints(app)

    # Return the instance
    return app