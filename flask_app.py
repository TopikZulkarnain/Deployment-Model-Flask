
# A very simple Flask Hello World app for you to get started with...

#from flask import Flask
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []

    # Make prediction using model loaded from disk as per the data.
    for data in datas:
        prediction = model.predict([np.array([data["LIMIT_BAL"],data["MARRIAGE"],data["EDUCATION"],data["SEX"],data["AGE"]])])

        # Take the first value of prediction
        output = prediction[0]
        out = 'pass' if output==1 else 'not pass'
        pred.append(out)
    return jsonify(pred)