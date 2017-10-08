from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success/<name><email>')
def create_success(name,email):
    return render_template("success.html", username = name, email = email)

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/success/' + name + email)

app.run(debug=True) 