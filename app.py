from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<a href='/greet'>Hello Universe!</a>"

@app.route('/greet')
def greet():
    return "<p>How are you?</p>"

@app.route('/knock-knock')
def knock_knock():
    return "<p>Who's there?</p>"

@app.route('/sample')
def sample():
    return "<p>sample</p>"
    
# Aku Buduy

#test only

#hello