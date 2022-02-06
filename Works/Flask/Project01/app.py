
from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

class Skil:
    def __init__(self,_id,_img,_title):
      self.id=_id
      self.img=_img
      self.title=_title
  
skil=[
  Skil(
   random.randint(1, 1000),
   'https://icon-library.com/images/html5-icon/html5-icon-13.jpg',
   "HTML"
  ),
   Skil(
   random.randint(1, 1000),
   'https://hackwild.com/static/brand-logos/css-logo.svg',
   "CSS"
  ),
    Skil(
   random.randint(1, 1000),
   'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/480px-Unofficial_JavaScript_logo_2.svg.png',
   "Javascript"
  ),
     Skil(
   random.randint(1, 1000),
   'https://cdn.worldvectorlogo.com/logos/bootstrap-5-1.svg',
   "Bootstarp"
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
      "https://lmpixels.com/demo/unique/unique-vcard/images/testimonials/testimonial_photo_2.jpg",
      "Nurlan Cahangirov"
  ),
   Testimonial(
      random.randint(1, 1000),
      "My first comment",
      "https://lmpixels.com/demo/unique/unique-vcard/images/testimonials/testimonial_photo_3.jpg",
      "Vüqar Cümşüdlü"
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
    "https://www.betterteam.com/images/web-developer-job-description-6494x4331-2020128.jpeg?crop=4:3,smart&width=1200&dpr=2",
    "Web proqramlaşdırma nədir?",
    "28.01.2022"
  ),
   Blog(
    random.randint(1, 1000),
    "https://resources.workable.com/wp-content/uploads/2019/07/temp_remote_work-01.png",
    "Remote iş modeli haqqında məlumat",
    "28.01.2022"
  ),
   Blog(
    random.randint(1, 1000),
    "https://res.cloudinary.com/gurucom/images/w_770,h_515,c_fill,g_auto/dpr_2/dpr_2/f_auto,q_auto/v1630998719/wordpress/blog/average-cost-of-a-freelance-web-developer/average-cost-of-a-freelance-web-developer-770x515.jpg?_i=AA",
    "Freelance işləməyin 5 ən böyük üstün cəhəti",
    "28.01.2022"
  )             
]

class Portfolio:
  def __init__(self,_id,_img):
    self.id=_id
    self.img=_img
      
portfolio=[
  Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
   Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
    Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
     Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
   Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
    Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
     Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
   Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  ),
    Portfolio(
    random.randint(1, 1000),
    "https://lmpixels.com/demo/unique/unique-vcard/images/portfolio/1.jpg"
  )
]

class Education:
  def __init__(self,_id,_date,_title,_edu,_shortinfo):
    self.id=_id
    self.date=_date
    self.title=_title
    self.edu=_edu
    self.shortinfo=_shortinfo
    
education=[
  Education(
    random.randint(1, 1000),
    "2010",
    "Specialization Course",
    "University of Studies",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  ),
  Education(
    random.randint(1, 1000),
    "2010",
    "Specialization Course",
    "University of Studies",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  ),
  Education(
    random.randint(1, 1000),
    "2010",
    "Specialization Course",
    "University of Studies",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  )
]


class Experience:
  def __init__(self,_id,_date,_title,_edu,_shortinfo):
    self.id=_id
    self.date=_date
    self.title=_title
    self.edu=_edu
    self.shortinfo=_shortinfo
    
experience=[
  Experience(
    random.randint(1, 1000),
    "Dec 2012 - Current",
    "Frontend-developer",
    "Web Agency",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  ),
  Experience(
    random.randint(1, 1000),
    "Dec 2012 - Current",
    "Frontend-developer",
    "Web Agency",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  ),
  Experience(
    random.randint(1, 1000),
    "2010",
    "Specialization Course",
    "University of Studies",
    "Mauris magna sapien, pharetra consectetur fringilla vitae, interdum sed tortor."  
  )
]
@app.route("/")  
def hello_World():
  return render_template("index.html",allskil=skil,alltestimonial=testimonial,allblog=blog,allportfolio=portfolio,alleducation=education,allexperience=experience)


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
    return render_template("formdata.html", messages=mesaj )
     
  return render_template("formdata.html")

if __name__=="__main__":
  app.run(debug=True)