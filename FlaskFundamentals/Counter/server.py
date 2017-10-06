from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'secretkey'


@app.route('/')
def index():
    if session.has_key('count') == False:
        session['count'] = 0
    return render_template('index.html', count= session['count'])

@app.route('/increment', methods=['POST'])
def increment():
    session['count'] += 2
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)