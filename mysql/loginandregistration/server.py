from flask import Flask, render_template, redirect, request, flash, session
# import the Connector function
from mysqlconnection import MySQLConnector
import md5
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'registration')
# an example of running a query
# print mysql.query_db("SELECT * FROM users")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    successful = True
    if len(first_name) < 2 or any(str.isdigit(char) for char in str(first_name)):
        flash('First name must contain only letters and be at least two characters')
        successful = False
    if len(last_name) < 2 or any(str.isdigit(char) for char in str(last_name)):
        flash('Last name must contain only letters and be at least two characters')
        successful = False
    if '@' not in str(email) or '.' not in str(email):
        flash('Email not valid')
        successful = False
    if len(password) < 8 or len(password) > 14:
        flash('Password must be between 8 - 14 characters')
        successful = False
    if password != confirm_password:
        flash('Please make sure your passwords match!')
        successful = False
    if successful == True:
        flash('Succesful Registration!')
        hashed_password = md5.new(password).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES('{}', '{}', '{}', '{}')".format(first_name, last_name, email, hashed_password)
        users = mysql.query_db(query)
        session['name'] = first_name
        return redirect('/success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    hashed_password = md5.new(password).hexdigest()
    query = "SELECT email FROM users WHERE email = '{}' and password = '{}'".format(email, hashed_password)
    login_email = mysql.query_db(query)
    query_2 = "SELECT password FROM users WHERE email = '{}' and password = '{}'".format(email, hashed_password)
    login_password = mysql.query_db(query_2)
    query_3 = "SELECT first_name FROM users WHERE email = '{}' and password = '{}'".format(email, hashed_password)
    login_name = mysql.query_db(query_3)
    print login_email[0]['email']
    print login_password
    if login_email[0]['email'] == email and login_password[0]['password'] == hashed_password:
        flash('Successful Log In! Welcome Back!')
        session['name'] = login_name[0]['first_name']
        return redirect('/success')
    else:
        flash('We could not process your log in information')
        return redirect('/')       
    
@app.route('/success')
def success():
    if session.has_key('name') == False:
        session['name'] = 'Stranger'
    return render_template('success.html', name = session['name'])



app.run(debug=True)