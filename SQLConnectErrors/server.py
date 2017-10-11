from flask import Flask, render_template, redirect, request
# import the Connector fu, nction
from mysqlconnection  import MySQLConnector
import datetime

app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'lead_gen_business')   #database
# an example of running a query
print mysql.query_db("SELECT * FROM friends")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_friend', methods=['POST'])
def create():
    name= request.form['name']
    age= request.form['age']
    created_at=datetime.datetime.now()
    mysql.query_db("INSERT INTO friends (name,age) VALUES ('{}',{}')".format(name,age))
    print name,age
    return redirect('/')

app.run(debug=True)