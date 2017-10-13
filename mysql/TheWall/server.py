from flask import Flask, render_template, redirect, request, flash, session
# import the Connector function
from mysqlconnection import MySQLConnector
import md5
import time
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'wall')
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
    created_at = time.strftime("%Y-%m-%d %H:%M")
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
        # flash('Succesful Registration!')
        hashed_password = md5.new(password).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES('{}', '{}', '{}', '{}', '{}')".format(first_name, last_name, email, hashed_password, created_at)
        users = mysql.query_db(query)
        session['name'] = first_name
        session['user_email'] = email
        return redirect('/wall')
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
    if login_email[0]['email'] == email and login_password[0]['password'] == hashed_password:
        # flash('Successful Log In! Welcome Back!')
        session['name'] = login_name[0]['first_name']
        session['user_email'] = login_email[0]['email']
        return redirect('/wall')
    else:
        flash('We could not process your log in information')
        return redirect('/')       

@app.route('/wall')
def wall():
    if session.has_key('name') == False:
        session['name'] = 'Stranger'
    # DOUBLE JOIN TABLES
    query = "SELECT concat(first_name, ' ', last_name) as full_name, concat(monthname(messages.created_at), ' ', day(messages.created_at), ' ', hour(messages.created_at), ':', minute(messages.created_at)) as posted_time, messages.id, message, messages.created_at FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at ASC"
    all_messages = mysql.query_db(query)
    name = session['name']
    query_2 = "SELECT concat(first_name, ' ', last_name) as full_name, concat(monthname(comments.created_at), ' ', day(comments.created_at), ' ', hour(comments.created_at), ':', minute(comments.created_at)) as posted_time, comments.message_id, comment, comments.created_at FROM comments JOIN messages ON messages.id = comments.message_id JOIN users ON users.id = comments.user_id ORDER BY comments.created_at ASC"
    all_comments = mysql.query_db(query_2)
    datetime = time.strftime("%H:%M")
    return render_template('wall.html', **locals())

@app.route('/messagepost', methods=['POST'])
def messagepost():
    message = str(request.form['new_message'])
    created_at = str(time.strftime("%Y-%m-%d %I:%M"))
    query = "SELECT id FROM users WHERE email = '{}'".format(session['user_email'])
    user_id = mysql.query_db(query)
    query_2 = 'INSERT INTO messages(message, created_at, user_id) VALUES ("{}", "{}", "{}")'.format(message, created_at, user_id[0]['id'])
    added_message = mysql.query_db(query_2)
    return redirect('/wall')

@app.route('/commentpost', methods=['POST'])
def commentpost():
    comment = str(request.form['new_comment'])
    created_at = time.strftime("%Y-%m-%d %I:%M")
    message_id = request.form['hidden_message']
    query = "SELECT id FROM users WHERE email = '{}'".format(session['user_email'])
    user_id = mysql.query_db(query)
    query_2 = 'INSERT INTO comments(comment, created_at, user_id, message_id) VALUES ("{}", "{}", "{}", "{}")'.format(comment, created_at, user_id[0]['id'], message_id)
    added_comment = mysql.query_db(query_2)
    return redirect('/wall')

@app.route('/logout', methods=["POST"])
def logout():
    session['name'] = ''
    session['user_email'] = ''
    return redirect('/')

app.run(debug=True)