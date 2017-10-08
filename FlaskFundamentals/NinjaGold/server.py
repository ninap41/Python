from flask import Flask, render_template, request, redirect,session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'secretkey'

timestamp = datetime.datetime.now()


@app.route('/')
def index():
    if session.has_key('gold') == False: ## sets session and gold
        session['gold'] = 0
    if session.has_key('activities') == False:
        session['activities'] = []
    print datetime.datetime.now()
    
    return render_template('index.html')

@app.route('/processgold', methods=['POST'])
def add_gold():
   
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the farm! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])  
        print session['activities']
        return redirect('/')
    elif request.form['building'] == 'cave':
        gold = random.randrange(5,10)
        session['gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the cave! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])  
        print session['activities']
        return redirect('/')
    elif request.form['building'] == 'house':
        gold = random.randrange(2,5)
        session['gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the house (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])  
        print session['gold']
        print session['activities']
        return redirect('/')
    elif request.form['building'] == 'casino':
        gold = random.randrange(-50,50)
        if gold < 0:     
            session['log'] = 'Lost ' + str(gold) + ' gold from the casino! (' + str(datetime.datetime.now()) + ')'
            session['gold'] += gold
        else:
            session['log'] = 'Earned ' + str(gold) + ' gold from the casino! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log']) 
        print session['activities'] 
        print session['gold']
        return redirect('/')
    else:
        session['log'] = 'Earned ' + str(gold) + ' gold from the casino! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])
            
    
    return redirect('/')


app.run(debug=True)


