from flask import Flask, jsonify
from flask import Flask
from flask_migrate import Migrate
import logging
from models import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

try:
    db.init_app(app)
    logging.info("Database initialized")
except Exception as e:
    logging.error(f"Error initializing database: {e}")


if __name__ == '__main__':
    app.run(port=5555)
