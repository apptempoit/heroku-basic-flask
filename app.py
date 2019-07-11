from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


from flask import Flask, request, redirect, url_for, flash, jsonify
from flask import request


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    modelfile = 'final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return ("<h1>Hello %s!! </h1>" % prediction)


@app.route('/createcm/<summary>/<change>')
def createcm(summary=None, change=None):
    return ("<h1>Hello %s!! </h1>" % summary)
    
@app.route('/golf')

def hello_world():  #def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
   return 'Hello World' #ให้แสดงข้อความว่า Hello World ออกทางหน้าฟอร์ม

@app.route('/data', methods=['GET'])
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    return ("<h1>Hello %s!! </h1>" % user)


@app.route('/parameters', methods=['GET'])
def query_strings():

    args1 = request.args['args1']
    args2 = request.args['args2']
    args3 = request.args['args3']

    return '''<h1>The Query String are...{}:{}:{}</h1>''' .format(args1,args2,args3)


@app.route('/button')
def button():  
   return '<form action="https://pythonc3.herokuapp.com/data">user <input type="text" name="user" ><br>x1 <input type="text" name="x1" <br><input type="submit" value="Submit"></form>'

if __name__ == '__main__':
    app.run()
