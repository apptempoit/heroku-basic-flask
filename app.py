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

@app.route('/button')
def button():  
   return '<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"><a href"https://pythonc3.herokuapp.com/createcm/25/25" class="w3-btn w3-blue">ส่งค่า</a>'

if __name__ == '__main__':
   app.run()
