
from flask import Flask, render_template
import random
app = Flask(__name__)

class Skil:
    def __init__(self,_id,_img,_title):
      self.id=_id,
      self.img=_img,
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
    
@app.route("/")  
def hello_World():
  return render_template("index.html",allskil=skil)


if __name__=="__main__":
  app.run(debug=True)