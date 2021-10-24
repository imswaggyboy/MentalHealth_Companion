
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

import mysql.connector
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os


app = Flask(__name__, template_folder='templates')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pravin'
#d = SQLAlchemy(app)
app.secret_key=os.urandom(24)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
conn=mysql.connector.connect(host="localhost",user="root",password="", db="prawjal")#,db="prajwal")

cursor=conn.cursor()

'''
class Contact(d.Model):
    sr, name, phone_num, email, msg, dt
    sr = d.Column(d.Integer, primary_key=True)
    name = d.Column(d.String(80), nullable=False)
    phone_num = d.Column(d.String(12), nullable=False)
    email = d.Column(d.String(20), nullable=False)
    msg = d.Column(d.String(120), nullable=False)
    dt = d.Column(d.String(12), nullable=False)
'''


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/login')
def login():
    #form = LoginForm()
    return render_template('login.html')#form=form)


@app.route('/login_validation', methods=['POST', 'GET'])
def login_validaation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/index.html')
    else:
         return redirect('/login')

@app.route('/contact.html', methods=['POST','GET'])
def contact():
    name=request.form.get('uname')
    phone=request.form.get('uphone')
    msg=request.form.get('umessage')
    cursor.execute("""INSERT INTO `contact`(`name`,`phone_num`,`msg`) VALUES
    ('{}','{}','{}')""".format(name,phone,msg))
    conn.commit()
    return render_template('contact.html')


'''
@app.route('/contact.html', methods = ['POST'])
def contact():
    if (request.method=='POST'):
        #add entry to the database
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num=phone, email=email, msg=message)
        d.session.add(entry)
        d.session.commit()
        return render_template('contact.html')
    else:
        return redirect('/')
'''





@app.route('/new_user', methods=['POST'])
def new_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""INSERT INTO `users`(`name`,`email`,`password`) VALUES
    ('{}','{}','{}')""".format(name,email,password))
    conn.commit()

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    return redirect('/accountopened')


@app.route('/accountopened', methods=['GET'])
def accountopened():
    return render_template('successful.html')

@app.route('/signup')
def signup():

    return render_template('signup.html', title='Signup')#,form=form)


@app.route('/taketest',methods=['GET'])
def taketest():
    if 'user_id' in session:
        return render_template('taketest.html')
    else:
        return redirect('/login')




standard_to = StandardScaler()
@app.route('/predict', methods=['POST'])


def predict():
    if request.method == 'POST':
        wind_down = float(request.form['wind_down'])
        dryness_mouth = int(request.form['dryness_mouth'])
        no_positive_feeling = int(request.form['no_positive_feeling'])
        breathing_difficulty = int(request.form['breathing_difficulty'])
        difficult_to_work = int(request.form['difficult_to_work'])
        over_react = int(request.form['over_react'])
        trembling = int(request.form['trembling'])
        use_nervous_energy = int(request.form['use_nervous_energy'])
        panic = int(request.form['panic'])
        nothing_look_forward = int(request.form['nothing_look_forward'])
        agitated = int(request.form['agitated'])
        difficult_relax = int(request.form['difficult_relax'])
        blue = int(request.form['blue'])
        intolerant = int(request.form['intolerant'])
        close_panic = int(request.form['close_panic'])
        unable_enthusiatic = int(request.form['unable_enthusiatic'])
        not_worth_person = int(request.form['not_worth_person'])
        touchy = int(request.form['touchy'])
        action_of_heart_abs = int(request.form['action_of_heart_abs'])
        scared_no_reason = int(request.form['scared_no_reason'])
        life_meaningless = int(request.form['life_meaningless'])

        prediction=model.predict([[wind_down, dryness_mouth, no_positive_feeling,breathing_difficulty, 
        difficult_to_work, over_react, trembling,use_nervous_energy, panic, nothing_look_forward, 
        agitated,difficult_relax, blue, intolerant, close_panic,unable_enthusiatic, not_worth_person, 
        touchy,action_of_heart_abs, scared_no_reason, life_meaningless]])
        output=round(prediction[0])
        if output<=0:
            return render_template('verylow.html')#,prediction_text="you are Normal")
        else:
            return render_template('moderate.html')#,prediction_text="you are Abnormal".format(output))
    else:
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)




'''

import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='prawjal',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
'''