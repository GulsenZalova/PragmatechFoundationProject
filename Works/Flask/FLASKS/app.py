from flask import Flask,render_template
import random
app=Flask(__name__)
class News:
    def __init__(self,_id,_title,_img,_shortİnfo,_detail):
        self.id=_id
        self.title=_title
        self.img=_img
        self.info=_shortİnfo
        self.detail=_detail
  
news=[
     News(
      random.randint(1,1000),
      "My first title",
      "https://cdn.britannica.com/q:60/88/194588-050-967E8D17/flowers.jpg",
      "My first shortinfo",
      "My first detail"   
    ),
     News(
      random.randint(1,1000),
      "My second title",
      "https://cdn.pixabay.com/photo/2013/07/21/13/00/rose-165819__340.jpg",
      "My second shortinfo",
      "My second detail"   
    )
     
]
@app.route('/')
def home():
    return render_template('index.html',allnews=news)
  
@app.route('/single')
def single():
    return render_template('single.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)