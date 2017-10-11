from flask import Flask, render_template, redirect, request, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import time
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'lead_gen_business')
# an example of running a query
# print mysql.query_db("SELECT * FROM countries")

entered_emails = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=["POST"])
def create_friend():
    email = request.form['email']
    timey_turner = time.strftime('%Y-%m-%d %H:%M')
    query = "SELECT email FROM clients WHERE email = '{}'".format(email)
    clients = mysql.query_db(query)
    log_in_time = email + ' ' + timey_turner
    if clients:
        flash('SUCCESS!')
        entered_emails.append(log_in_time)
        return redirect('/results')
    else:
        flash('EMAIL IS NOT VALID')
        return redirect('/')

@app.route('/results')
def success():
    return render_template('/results.html', all_clients = entered_emails)

app.run(debug=True)