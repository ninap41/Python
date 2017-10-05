from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def create_user():
    print "wanna be a ninja?"
    return render_template('/ninjas.html')

@app.route('/dojo/new')
def create_ninjas():
    return render_template("dojos.html")









app.run(debug=True) 