#-*- coding=utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/<string:name>')
def Home(name):
    return ("<h1>Hello %s!! </h1>" % name)

@app.route('/createcm/<summary>/<change>')
def createcm(summary=None, change=None):
    return ("<h1>Hello %s!! </h1>" % summary)
    
@app.route('/golf')

def hello_world():  #def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
   return 'Hello World' #ให้แสดงข้อความว่า Hello World ออกทางหน้าฟอร์ม


@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    return ("<h1>Hello %s!! </h1>" % user)

@app.route('/button')
def button():  
   return '<form action="https://pythonc3.herokuapp.com/data">user <input type="text" name="user" ><br>x1 <input type="text" name="x1" <br><input type="submit" value="Submit"></form>'

if __name__ == '__main__':
   app.run()
