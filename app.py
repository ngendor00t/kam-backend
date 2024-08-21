from flask import Flask, jsonify
from flask import Flask
from flask_migrate import Migrate

from models import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

db.init_app(app)



if __name__ == '__main__':
    app.run(port=5555)
