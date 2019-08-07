from flask import Flask, request, redirect, url_for, flash, jsonify , render_template
import numpy as np
import pickle as pickle
import json
from numpy.core import multiarray

#app = Flask(__name__)


#@app.route('/api/', methods=['POST'])
#def makecalc():
#    data = request.get_json()
#    modelfile = 'final_prediction.pickle'
#    model = p.load(open(modelfile, 'rb'))
#    prediction = np.array2string(model.predict(data))

#    return jsonify(prediction)

#if __name__ == '__main__':
#    app.run(debug=True)

    
    
    
app=Flask(__name__)

#@app.route('/')
@app.route('/')
def index():
    return render_template('index.html')


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("DT_model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction=result
        return render_template("result.html",prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
