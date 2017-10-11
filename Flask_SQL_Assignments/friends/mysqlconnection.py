from flask import Flask, render_template, redirect, request
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime
import time
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# print mysql.query_db("SELECT * FROM countries")
print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    query = "SELECT id, name, age, concat( monthname(created_at), ' ', Day(created_at)) as friend_date, year(created_at) as year_name FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    name = request.form['name']
    age = request.form['age']
    created_at = time.strftime('%Y-%m-%d')
    print name, age, created_at
    mysql.query_db("INSERT INTO friends (name, age, created_at) VALUES ('{}', {}, '{}')".format( name, age, created_at))
    return redirect('/')




app.run(debug=True)