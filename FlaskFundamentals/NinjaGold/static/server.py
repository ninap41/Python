from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guessing():
  
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    
    return redirect('/')

app.run(debug=True)
