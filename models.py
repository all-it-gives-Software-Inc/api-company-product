import datetime
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    database_name ='postgres'
    default_database_path= "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)
    database_path = os.getenv('DATABASE_URL', default_database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
'''

    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

class Store(db.Model):
    __tablename__ = 'store'
    id = Column(String, primary_key=True)
    name = Column(String(255), unique=True)
    category = Column(String(255))
    delivery_estimate = Column(String(255))
    rating = Column(String(255))
    image_path = Column(String(255))
    about = Column(String(255))
    hours = Column(String(255))
    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'deliveryEstimate': self.delivery_estimate,
            'rating': self.rating,
            'imagePath': self.image_path,
            'about': self.about,
            'hours': self.hours,
        }
    def __init__(self, id,name, category,delivery_estimate,rating,image_path,about,hours):
        self.id = id
        self.name = name
        self.category = category
        self.delivery_estimate = delivery_estimate
        self.rating = rating
        self.imagePath = image_path
        self.about = about
        self.hours = hours
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()