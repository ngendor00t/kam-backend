from flask import Flask
from flask_migrate import Migrate

from models import db,Country,exportproduct,

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)




if __name__ == '__main__':
    app.run(port=5555)
