
from flask import Flask, render_template
import random
app = Flask(__name__)

class Skil:
    def __init__(self,_id,_img,_title):
      self.id=_id
      self.img=_img
      self.title=_title
  
skil=[
  Skil(
   random.randint(1, 1000),
   'https://image.freepik.com/free-vector/garden-flowwer-logo_8855-156.jpg',
   "HTML"
  ),
   Skil(
   random.randint(1, 1000),
   'https://image.freepik.com/free-vector/garden-flowwer-logo_8855-156.jpg',
   "Javascript"
  ),
    Skil(
   random.randint(1, 1000),
   'https://image.freepik.com/free-vector/garden-flowwer-logo_8855-156.jpg',
   "Bootstrap"
  ),
     Skil(
   random.randint(1, 1000),
   'https://image.freepik.com/free-vector/garden-flowwer-logo_8855-156.jpg',
   "CSS"
  ), 
     Skil(
   random.randint(1, 1000),
   'https://image.freepik.com/free-vector/garden-flowwer-logo_8855-156.jpg',
   "CSS"
  )  
]

class Testimonial :
  def __init__(self,_id,_shortİnfo,_img,_ad):
      self.id=_id
      self.info=_shortİnfo
      self.img=_img
      self.ad=_ad
    
testimonial=[
  Testimonial(
      random.randint(1, 1000),
      "My first comment",
      "https://lmpixels.com/demo/unique/unique-vcard/images/testimonials/testimonial_photo_1.jpg",
      "Aytac Hüseynova"
  ),
   Testimonial(
      random.randint(1, 1000),
      "My first comment",
      "https://lmpixels.com/demo/unique/unique-vcard/images/testimonials/testimonial_photo_1.jpg",
      "Aytac Hüseynova"
  )
]

class Blog:
  def __init__(self,_id,_img,_title,_date):
    self.id=_id
    self.img=_img
    self.title=_title
    self.date=_date
    
blog=[
  Blog(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/testimonials/testimonial_photo_1.jpg",
    "Mənim ilk blogum",
    "28.01.2022"
  )      
]

    
@app.route("/")  
def hello_World():
  return render_template("index.html",allskil=skil,alltestimonial=testimonial,allblog=blog)
if __name__=="__main__":
  app.run(debug=True)