from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/')
def index():
    crud = randint(0,10)
    return str(crud)

@app.route('/hello')
def hello():
    return 'Hello World'
	
if __name__ == '__main__':
    app.run()