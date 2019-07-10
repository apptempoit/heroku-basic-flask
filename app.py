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

if __name__ == '__main__':
   app.run()
