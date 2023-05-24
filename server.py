from flask import Flask
import 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll_dice')
def roll():
    return f'{random.randint(1,6)}, {random.randint(1,6)}, {random.randint(1,6)}'