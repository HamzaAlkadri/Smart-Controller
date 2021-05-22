#py -m venv env#
#key for installing the env#
#.\env\Scripts\activate#
#the starting key for the enviroment ya 7omar^#
#Ctrl+Shift+P and then Terminal: Relaunch Active Terminal#to force reload
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
relayState1 = True
relayState2 = True
relayState3 = True
relayState4 = True
class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
#Pyrebase setup tings
import pyrebase



firebase = pyrebase.initialize_app(config)
database=firebase.database()
#the magic yazeed did to make this thing work
def stream_handler1(message):
    print(message) 
    global relayState1
    global relayState2
    global relayState3
    global relayState4
    if message["path"]=="/":
        relayState1=message["data"]['relayState1']
        relayState2=message["data"]['relayState2']
        relayState3=message["data"]['relayState3']
        relayState4=message["data"]['relayState4']
    if message["path"]=="/relayState1":
        relayState1=message["data"]
    elif message["path"]=="/relayState2":
        relayState2=message["data"]
    elif message["path"]=="/relayState3":
        relayState3=message["data"]
    elif message["path"]=="/relayState4":
        relayState4=message["data"]
my_stream = database.child("/relays").stream(stream_handler1)



#  def __repr__(self): 
#        return '<Task %r>' %self.id

from flask import render_template, flash, redirect, url_for



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
    #more magic yazeed did to make this work!
    database.child('/relays').update({'relayState1':relayState1})
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
    #Hamza trying to make this thing work
    database.child('/relays').update({'relayState2':relayState2})
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
    database.child('/relays').update({'relayState3':relayState3})
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
    database.child('/relays').update({'relayState4':relayState4})
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
    app.run(debug=True, host='192.168.1.18', port=8080)