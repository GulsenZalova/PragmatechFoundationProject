from run import app
from flask import render_template

@app.route("/admin", methods=['GET','POST'])  
def admin_index():
  return render_template("admin/base.html")