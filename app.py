from flask import Flask, session, request, url_for, redirect, render_template
from utils import db_utils

app = Flask(__name__)

@app.route('/')
@app.route('/update/')
def update():
    return 

@app.route('/add/')
def add():
    return render_template("add.html")

@app.route('/list/')
def list():
    return

@app.route('/items/')
def items():
    return render_template("items.html")

@app.route('/manage/')
def manage():
    return

if __name__ == '__main__':
    app.run(debug=True)
