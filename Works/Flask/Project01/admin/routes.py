# admin/routes

import flask
from run import app 
from flask import Flask,render_template,url_for,redirect,request
from models import *

@app.route("/admin", methods=['GET','POST']) 
def admin():
  return render_template("admin/base.html")

@app.route("/admin/about", methods=['GET','POST'])  
def about():
  from models import About
  from run import db
  import os
  from werkzeug.utils import secure_filename
  about = About.query.all()
  if request.method=='POST':
    file = request.files['about_img']
    filename = secure_filename(file.filename)   
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    about_title = request.form["about_title"]
    abt = About(
      about_img = os.path.join(app.config['UPLOAD_FOLDER'], filename),
      about_title = about_title
    )
    db.session.add(abt)
    db.session.commit()
    return redirect("/admin")
  return render_template("admin/about.html",about=about)

@app.route("/aboutDelete/<int:id>",methods=["GET","POST"])

def about_delete(id):
    from models import About
    import os
    from run import db
    abt = About.query.filter_by(id=id).first()
    filename = abt.about_img
    # os.unlink(os.path.join(filename))
    db.session.delete(abt)
    db.session.commit()
    return redirect ("/admin/about")
