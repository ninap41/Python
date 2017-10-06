from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/groupninja')
def ninja():
  return render_template("groupninja.html")


app.run(debug=True) 