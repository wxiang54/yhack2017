from flask import Flask, session, request, url_for, redirect, render_template
from utils import db_utils

app = Flask(__name__)

@app.route('/')
@app.route('/update/')
def update():
    return render_template('update.html')

@app.route('/add/')
def add():
    return render_template("add.html")

@app.route('/add-category/')
def add_category():
    return render_template("")

@app.route('/list/')
def list():
    return render_template('list.html')

@app.route('/items/')
def items():
    return render_template("items.html")

@app.route('/manage/')
def manage():
    return render_template('manage.html')

if __name__ == '__main__':
    app.run(debug=True)
