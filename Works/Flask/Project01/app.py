from flask import Flask,render_template

app=Flask(__name__)
isciler=[
    { "Vəzifə":"Müdir",
      "Maaş":"2000AZN",    
    },
    { "Vəzifə":"Call-Center",
      "Maaş":"300AZN",    
    },
     { "Vəzifə":"Təcrübəçi",
      "Maaş":"100AZN",    
    }
    
]
@app.route('/')
def home():
    return render_template('index.html',data=isciler)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)