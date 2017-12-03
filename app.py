from flask import Flask, session, request, url_for, redirect, render_template
from utils import db_utils

app = Flask(__name__)

@app.route('/')
@app.route('/update/')
def update():
    return 

@app.route('/add/')
def add():
    return

@app.route('/list/')
def list():
    return

@app.route('/items/')
def items():
    return

@app.route('/manage/')
def manage():
    return

if __name__ == '__main__':
    app.run()
