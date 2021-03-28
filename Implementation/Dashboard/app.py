from flask import Flask, request, url_for, redirect, render_template, jsonify
from flask import Flask
from pycaret.regression import*
import pandas as  pd
import pickle
import numpy as np
app = Flask(__name__, template_folder='templates')

model=load_model('deployment_28042020')
cols=['age','sex','bmi','children','smoker','region']

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final=np.array(int_features)
    data_unseen=pd.DataFrame([final],columns=cols)
    prediction= predict_model(model, data=data_unseen, round=0)
   # prediction=int(prediction.label[0])
    print(prediction)
    return render_template('home.html',output='Expected Bill willbe {}'.format(prediction))
   #return "hellow"

if __name__ == '__main__':
    app.run( debug=True)