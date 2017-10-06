from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', counter)
def index():
    return ("counter.html")

@app.route('/', methods=['POST'])
def index():
    if request.form['action'] == 'visited':
        visits+=
    return render_template("counter.html", visits=visits)

app.run(debug=True) 