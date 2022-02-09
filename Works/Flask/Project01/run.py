from flask import Flask, render_template,request
import random
from datetime import date

app = Flask(__name__)

# from controllers.admin_routes import *
# from controllers.app_routes import *

mesajlar=[]
@app.route("/", methods=['GET','POST'])  
def add():
  return render_template("index.html")
  
@app.route("/messages",methods=['GET','POST'])  
def messages():
  if request.method=="POST":
    _ad=request.form["ad"]
    _email=request.form["email"]
    _mesaj=request.form["mesaj"]
    _tarix=datetime.date.today 
    mesaj={
      "ad":_ad,
      "email":_email,
      "mesaj":_mesaj,
      "tarix":_tarix 
    }
    mesajlar.append(mesaj)
    return render_template("formdata.html", messages=mesajlar)

  return render_template("formdata.html")
  # return render_template("formdata.html")

if __name__=="__main__":
  app.run(debug=True)