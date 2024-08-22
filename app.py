from flask import Flask, jsonify
from flask import Flask
from flask_migrate import Migrate
import logging
from models import db ,Country,Exportproduct,Importproduct



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


@app.route('/')
def home():
    return jsonify({'message': 'kenya association of manufacturers database'})

# @app.route('/exportproducts', method=['GET'])
# def get_export_products():
#     export_products= Exportproduct.query.all()
#     return jsonify([{'id': export_product.id, 'name': country}for Country in get_countries])


# @app.route('/countries', methods=['GET'])
# def get_countries():
#     countries = Country.query.all()
#     return jsonify([{'id': country.id, 'name': country.name}for country in countries])
# except Exception as e:
#     return jsonify({'error': str(e)}), 500
@app.route('/countries', methods=['GET'])
def get_countries():
    try:
        countries = Country.query.all()
        return jsonify([{'id': country.id, 'name': country.name} for country in countries])
    except Exception as e:
        print('Error', str(e))
        return jsonify({'error': str(e)}), 500
    


@app.route('/exportproducts', methods=['GET'])
def get_export_products():
    # Retrieve all export products from the database
    export_products = Exportproduct.query.all()
    
    # Prepare a list to hold the export product data
    export_product_data = []
    
    # Loop through each export product to format the data
    for product in export_products:
        export_product_info = {
            'id': product.id,
            'short_des': product.short_des,
            'quantity': product.quantity,
            'FOBvalue': product.FOBvalue,
            'unit': product.unit,
            'year': product.year,
            'country': product.country.name if product.country else 'No Country'  # Assuming 'name' is a field in Country model
        }
        export_product_data.append(export_product_info)
    
    # Return the export product data as JSON
    return jsonify(export_product_data)



    # Return the product data as JSON
    return jsonify(product_data)


if __name__ == '__main__':
    app.run(port=5555)
