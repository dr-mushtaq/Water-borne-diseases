from flask import Flask, request, url_for, redirect, session, render_template, jsonify
from flask import Flask
from pycaret.regression import*
import pandas as  pd
import pickle
import numpy as np
from flask_mysqldb import MySQL
import MySQLdb

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__, template_folder='templates')

app.secret_key="12345" # user for secure communication 
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "dashbaord"
db= MySQL(app)

model=load_model('malyria_classification')
cols=['MRNO','AGE','GENDER','DISTRICT','TEHSIL','REPORT_VERIFIED','CPT_ID', 'RESULT_VALUE','CPT_ID.1']

@app.route('/', methods=['GET','POST'])
@app.route('/loginp', methods =['GET', 'POST'])
def loginp():
    msg = ''
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username= request.form['username']
            password= request.form['password']
            cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT *FROM accounts WHERE username=%s AND password=%s",(username,password))
            info= cursor.fetchone()
            if info:
                session['id']=info['id']
                session['username']=info['username']
                msg = 'Logged in successfully !'
                #return render_template('index.html', msg = msg)
                return redirect("/index", code=302)
            else:
                msg = 'Incorrect username / password !'
            #if info['email'] == 'mushtaqmsit@gmail.com' and info['password'] == '123':
                # msg = 'Logged in successfully !'
                 #return render_template('index.html', msg = msg)
            #else:
               # return " login unsuccessful, please register"
            
    return render_template('login2.html')

# This cod used to link two Html pages through Flask
@app.route('/register2', methods=['GET', 'POST'])
def register():
    msg = ''
    #if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            db.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register2.html', msg = msg)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgotpassword():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('login'))

    # show the form, it wasn't submitted
    return render_template('forgot-password.html')

@app.route('/index')
def Malaria():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    # Find Total Malaria tested paitents
    Result_value='Y'
    cursor.execute("SELECT * FROM malaria WHERE Result = %s ", (Result_value,))
    Total_Malaria_tested_Case = cursor.fetchall()
    Malaria_tested=len(Total_Malaria_tested_Case)

    # Find Total  Nagtive Malaria Cases
    cursor_Malaria_postive_Cases = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_Postive='Positive'
    cursor_Malaria_postive_Cases.execute("SELECT * FROM malaria WHERE Result_txt = %s ", (Malaria_Postive,))
    Total_Malaria_Postive_Case = cursor_Malaria_postive_Cases.fetchall()
    Malaria_Postive_Cases_1=len(Total_Malaria_Postive_Case)

    # Malaria Negative Cases
    cursor_Malaria_Negative_Cases = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_Negative='Negative'
    cursor_Malaria_Negative_Cases.execute("SELECT * FROM malaria WHERE Result_txt = %s ", (Malaria_Negative,))
    Total_Malaria_Negative_Case = cursor_Malaria_Negative_Cases.fetchall()
    Malaria_Negative_Cases_1=len(Total_Malaria_Negative_Case)

    # Total Malaria Patient Postive Predicted Cases
    cursor_Malaria_pred_Cases = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_pred='Positive'
    cursor_Malaria_pred_Cases.execute("SELECT * FROM malaria WHERE Predicted_Result = %s ", (Malaria_pred,))
    Total_Malaria_pred_Case = cursor_Malaria_pred_Cases.fetchall()
    Malaria_pred_Cases_1=len(Total_Malaria_pred_Case)

    return render_template('index.html', Total_pred=Malaria_pred_Cases_1, Total_Malaria_Negative_Case2=Malaria_Negative_Cases_1, Total_Malaria_tested_Case1=Malaria_tested, Total_Malaria_Postive_Case2=Malaria_Postive_Cases_1)
    
@app.route('/Typhoid')
def Typhoid():
    #return render_template("home.html")
    return render_template('index2.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final=np.array(int_features)
    data_unseen=pd.DataFrame([final],columns=cols)
    prediction= predict_model(model, data=data_unseen, round=0)
   # prediction=int(prediction.label[0])
    print(prediction)
    return render_template('index.html',output=prediction)
   #return "hellow"


if __name__ == '__main__':
   app.run( debug=True)