from Model import District_dict
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
from flask import Flask,request,jsonify,render_template
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

#model=load_model('malyria_classification')
cols=['DISTRICT_Encoded','Age', 'Gender_Encoded']
model = pickle.load(open('model_rf2.pkl','rb'))

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

    # Find Total Postive Malaria Cases
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

    # New testing

    # Rank Negative Cases in Tehsil 
    cursor_Malaria_Tehsil_Cases22 = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_n22 ='Negative'
    #Tehsil='Havelia'
    #cursor_Malaria_Tehsil_Cases.execute("SELECT  Tehsil FROM malaria")
    cursor_Malaria_Tehsil_Cases22.execute("SELECT  Tehsil FROM malaria WHERE Result_txt = %s ", (Malaria_n22,))
    Total_Malaria_TEHSIL_Case22 = cursor_Malaria_Tehsil_Cases.fetchall()
    #Malaria_mytehsil_Cases_1=Total_Malaria_TEHSIL_Case
    print(Total_Malaria_TEHSIL_Case22)

    # New testing

    # Rank Postive Cases in Tehsil 
    cursor_Malaria_Tehsil_Cases33 = db.connection.cursor(MySQLdb.cursors.DictCursor)
    Malaria_n33 ='Positive'
    #Tehsil='Havelia'
    #cursor_Malaria_Tehsil_Cases.execute("SELECT  Tehsil FROM malaria")
    cursor_Malaria_Tehsil_Cases33.execute("SELECT Tehsil FROM malaria WHERE Result_txt = %s ", (Malaria_n22,))
    Total_Malaria_TEHSIL_Case33 = cursor_Malaria_Tehsil_Cases.fetchall()
    #Malaria_mytehsil_Cases_1=Total_Malaria_TEHSIL_Case
    print(Total_Malaria_TEHSIL_Case33)

    
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
    # Compare Total negative and Postive cases in districtu

    return render_template('index.html', Total_n1 = Total_Malaria_TEHSIL_Case22, Total_p1 =Total_Malaria_TEHSIL_Case33, x_gender=Gender_p_list, y_gender=gender_list, y=teshil_list, x=total_postive_list, Total_p=Malaria_mytehsil_Cases_1, Total_pred=Malaria_pred_Cases_1, Total_Malaria_Negative_Case2=Malaria_Negative_Cases_1, Total_Malaria_tested_Case1=Malaria_tested, Total_Malaria_Postive_Case2=Malaria_Postive_Cases_1)
    
@app.route('/Typhoid')
def Typhoid():
    #return render_template("home.html")
    return render_template('index2.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    print('size of input',len(int_features))
    #Tehsil_dict = {'havelia': 0, 'Abbottabad': 1, 'Dassu': 2, 'Oghi': 3, 'Haripur': 4}
    District_dict = { 'Abbottabad':0, 'Mansehra':1, 'Haripur':2, 'Kohistan':3, 'Peshawar':4, 'Batgram':5, 'Bolan':6, 'Shangla':7, 'RahimYar Khan':8, 'Mardan':9, 'MUZAFFARABAD':10, 'Lower Dir':11, 'DIAMIR':12, 'ISLAMABAD':13, 'Lasbela':14, 'GILGIT':15, 'Vehari':16, 'Swat':17, 'Swabi':18, 'Tharparkar':19,'BAGH':20, 'UNKNOWN F.A.T.A':21, 'Mianwali':22, 'Attock':23, 'Dadu':24, 'Charsadda':25, 'ORAKZAI':26, 'MIRPUR':27, 'KHYBER':28, 'Lahore':29, 'Upper Dir':30, 'Hangu':31, 'KURRAM':32, 'Zhob':33, 'POONCH':34,'Nowshera':35, 'Rawalpindi':36, 'MOHMAND':37}
    Gender_dict = { 'Male':1, 'Female':2, 'Neuter':3 }
    #Tehsil_value = int_features[0]
    District_value = int_features[1]
    Age_value = int_features[2]
    #date_value = int_features[2]
    Gender_value = int_features[3]
    

    #a= pd.Series(Tehsil_value)
    #Tehsil = a.map(Tehsil_dict).values[0]   #<----------
    b= pd.Series(District_value)
    District = b.map(District_dict).values[0]   #<----------
    c= pd.Series(Gender_value)
    Gender = c.map(Gender_dict).values[0]   #<----------  #<----------


    #day = int(pd.to_datetime(date_value, format="%Y-%m-%dT%H:%M").day)  
    #month = int(pd.to_datetime(date_value, format="%Y-%m-%dT%H:%M").month)  #<---------
    #hour = int(pd.to_datetime(date_value, format ="%Y-%m-%dT%H:%M").hour)
   # minute = int(pd.to_datetime(date_value, format ="%Y-%m-%dT%H:%M").minute)
    pred_features = [np.array([ District,Age_value, Gender])]
    #y333 = [x for x in pred_features if str(x) != 'nan']


    
    #X1=pred_features.fillna(0, inplace=True)
   # X1 = [0 if str(pred_features)=='nan' else pred_features for x in X1]

    prediction = model.predict(pred_features)
    output = prediction



    final=np.array(int_features)
    #data_unseen=pd.DataFrame([pred_features],columns=cols)
    #prediction= predict_model(model, data=data_unseen, round=0)
    #output=prediction
   # prediction=int(prediction.label[0])
   
  
    return render_template('index.html', pred='The Malaria result for the given paitent is:-  INR {}'.format(output), output=prediction)
   #return "hellow"

# plot and chart of 

if __name__ == '__main__':
   app.run( debug=True)