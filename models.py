from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


db = SQLAlchemy()

class Country (db.Model):
    __tablename__= 'countries'

    id = db.Column(db.Integer, primary_key=True)
    Countryname = db.Column(db.String(45), nullable=False)

    export_products = relationship('ExportProduct', back_populates='country')


class Exportproduct(db.Model):
    __tablename__='exportproducts'

    id = db.Column(db.Integer,primary_key=True)
    short_des= db.Column(db.String())
    quantity=db.Column(db.Integer())
    FOBvalue=db.Column(db.Integer())
    unit=db.Column(db.String())
    year=db.Column(db.Integer())


    country_id = db.Column(db.Integer, ForeignKey('countries.id'))
    country = db.relationship('Country', back_populates='export_products')



class Hsc (db.Model):
        __tablename__="Hscs"


        id = db.Column(db.Integer, primary_key=True)
        code = db.Column(db.Integer)




class Importproduct(db.Model):
     __tablename__= 'importproducts'

     id = db.Column(db.Integer, primary_key=True )