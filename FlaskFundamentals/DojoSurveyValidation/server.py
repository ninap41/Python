from flask import Flask, render_template, request, redirect, flash,  url_for
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/results', methods=['POST']) 
def create_process():
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comment = request.form['comment'] 
    if len(request.form['name']) == 0:
        flash('You did not enter a name')
    if len(request.form['location']) == 0:
        flash('you did not choose a location')
    if len(request.form['language']) == 0:
        flash('you did not choose a language')
    else:
        pass
    if len(request.form['comment']) > 120:
        flash('Comment is too long, no one will read this', 'commentError')  
    return render_template("result.html", name = name, location = location, language = language, comment = comment)

@app.route('/reset')
def reset():
    
    return render_template("/")

app.run(debug=True) 