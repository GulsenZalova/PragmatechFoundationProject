from run import db

# About
class About(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  about_img=db.Column(db.String(70))
  about_title=db.Column(db.String(70))