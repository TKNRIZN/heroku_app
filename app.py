from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from numpy.random import randint
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



db_url = "postgres://wfxuahnsnqwyhm:c7d92481620702345e579db7e72c497c161af360975b070a30fa261aece58a9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/das6kca5cp3976"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="hobbylist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


user = db.session.query(User).filter_by(id=1).first()
db.session.commit()


@app.route('/')
def index():
    return "HELLO"


@app.route('/v1/get_message',methods=["GET"])
def get_message():
    
    message = picked_up()
    return message



def picked_up():
    number = randint(1,100)
    user = db.session.query(User).filter_by(id=number).first()
    db.session.commit()
    return user.name



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
