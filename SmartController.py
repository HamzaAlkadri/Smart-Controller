
import pyrebase
import RPi.GPIO as GPIO
# Import sleep Module for timing
GPIO.setmode(GPIO.BCM)
# Disable Warnings
GPIO.setwarnings(False)
#Importing Button
from gpiozero import Button
firebase = pyrebase.initialize_app(config)
database=firebase.database()
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
def stream_handler1(message):
    print(message) 

    if message["path"]=="/":
        try:
            GPIO.output(22, message['data']['relayState1'])
        except:
            print()
        try:
            GPIO.output(23, message['data']['relayState2'])
        except:
            print()
        try:
            GPIO.output(24, message['data']['relayState3'])
        except:
            print()
        try:    
            GPIO.output(25, message['data']['relayState4'])
        except:
            print()
my_stream = database.child("/relays").stream(stream_handler1)
