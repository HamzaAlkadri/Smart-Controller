#.\env\Scripts\activate.ps1#
#the starting key for the enviroment ya 7omar^#
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)


#  def __repr__(self): 
#        return '<Task %r>' %self.id

from flask import render_template, flash, redirect, url_for
relayState1 = True
relayState2 = True
relayState3 = True
relayState4 = True


###################################################################################################################
@app.route('/relay1', methods=['POST'])
def relay1_toggle():
    global relayState1
    relayState1 = not relayState1
    message = ''
    if relayState1:
        message = '1off'
    else :
        message = '1on'
    print (message)
    return redirect ('/')
@app.route('/relay2', methods=['POST'])
def relay2_toggle():
    global relayState2
    relayState2 = not relayState2
    message = ''
    if relayState2:
        message = '2off'
    else :
        message = '2on'
    print (message)
    return redirect ('/')
@app.route('/relay3', methods=['POST'])
def relay3_toggle():
    global relayState3
    relayState3 = not relayState3
    message = ''
    if relayState3:
        message = '3off'
    else :
        message = '3on'
    print (message)
    return redirect ('/')
@app.route('/relay4', methods=['POST'])
def relay4_toggle():
    global relayState4
    relayState4 = not relayState4
    message = ''
    if relayState4:
        message = '4off'
    else :
        message = '4on'
    print (message)
    return redirect ('/')
###################################################################################################################
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_priority = request.form['priority']
        new_task = Todo(content=task_content,priority=task_priority)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
            
            
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', relayState1=relayState1, relayState2=relayState2, relayState3=relayState3, relayState4=relayState4) 

    

if __name__ == "__main__":
    app.run(debug=True)