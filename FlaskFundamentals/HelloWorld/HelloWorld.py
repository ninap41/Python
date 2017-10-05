from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return '<h1>Hello World</h1><p>my name is nina</p>'



app.run(debug=True)