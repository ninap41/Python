from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    return redirect('/process/' + name)

@app.route('/process/<name>')
def create_process(name):
    return render_template("process.html", username = name)

app.run(debug=True) 