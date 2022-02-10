from flask import Flask, render_template,request
import random
from datetime import date
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#app routes
from app.routes import *

#admin routes
from admin.routes import *

if __name__=='__main__':
  db.create_all()
  app.run(debug=True)