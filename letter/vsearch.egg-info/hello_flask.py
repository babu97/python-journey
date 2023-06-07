from flask import Flask 
from vsearch import search4letters
app = Flask(__name__)
@app.route('/')
def hello()-> str:
    return 'Hello world from flask!'
app.run()