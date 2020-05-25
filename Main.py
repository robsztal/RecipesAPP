from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://admin:Robotnik2500@recipesdb.ckpwdzaartyk.us-east-1.rds.amazonaws.com'
db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column('idx', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)