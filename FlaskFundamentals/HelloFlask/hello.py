from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return 'HOMIE'


@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/success')
def success():
  return render_template('success.html')



app.run(debug=True)