from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/English')
def EnglishGreeting():
    return 'Hello world, Welcome!'

@app.route('/Spanish')
def SpanishGreeting():
    return 'Hola!  Bienvenido!'