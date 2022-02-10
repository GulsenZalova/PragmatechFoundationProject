#app routes
from flask import render_template,redirect,url_for,request
from run import app

@app.route("/",methods=['GET','POST'])  
def app_index():
  from models import About
  about = About.query.all()
  return render_template("app/index.html",about=about)