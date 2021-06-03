from os import name
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

    # rank postive cases
    cursor_Malaria_Tehsil_Cases = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_psitve ='Positive'
    Tehsil='Havelia'
    cursor_Malaria_Tehsil_Cases.execute("SELECT  Tehsil FROM malaria")
    Total_Malaria_TEHSIL_Case = cursor_Malaria_Tehsil_Cases.fetchall()
    Malaria_mytehsil_Cases_1=Total_Malaria_TEHSIL_Case
    
    Malaria_P='Positive'
    conn = MySQLdb.connect("localhost", "root", "" , "dashbaord") 
    #cursor = db.connection.cursor(MySQLdb.cursors.DictCursor) 
    cursor = conn.cursor() 
    cursor.execute("select Tehsil,Result_txt, Gender from malaria WHERE Result_txt = %s ", (Malaria_P,) ) 
    
    data_ = cursor.fetchall() 
    x = [] 
    y = [] 
    z = []
    for i in data_: 
        x.append(i[0])	
        y.append(i[1])
        z.append(i[2])	
    
    from pandas import DataFrame
    df_x = DataFrame (x,columns=['tehsil'])
    df_y = DataFrame (y,columns=['postive'])
    df_z = DataFrame (z,columns=['gender'])
    df_x['cases']=df_y
    df_z['Cases1']=df_y
    #print(df_z.head())
    Count_total_Postivecases=df_x.groupby('tehsil')['cases'].size().reset_index(name='count')
    Count_total_Gender=df_z.groupby('gender')['Cases1'].size().reset_index(name='count')
    # Count total cases in tehsil
    tehsil1=Count_total_Postivecases['tehsil']
    total_cases=Count_total_Postivecases['count']
    teshil_list=tehsil1.values.tolist()
    total_postive_list= total_cases.values.tolist()
    # Count total postive cases as Gender
    Gender_name=Count_total_Gender['gender']
    Gender_total1=Count_total_Gender['count']
    gender_list=Gender_name.values.tolist()
    #Gender_p_list= gender_list.values.tolist()
    Gender_p_list= Gender_total1.values.tolist()
    print(gender_list)
    print(Gender_p_list)


    return render_template('index.html',x_gender=Gender_p_list, y_gender=gender_list, y=teshil_list, x=total_postive_list, Total_p=Malaria_mytehsil_Cases_1, Total_pred=Malaria_pred_Cases_1, Total_Malaria_Negative_Case2=Malaria_Negative_Cases_1, Total_Malaria_tested_Case1=Malaria_tested, Total_Malaria_Postive_Case2=Malaria_Postive_Cases_1)
    
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

# plot and chart of 

if __name__ == '__main__':
   app.run( debug=True)