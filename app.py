from flask import Flask, session, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/update/')
def update():

@app.route('/add/')
def add():

@app.route('/list/')
def list():

@app.route('/items/')
def items():

@app.route('/manage/')
def manage():

if __name__ == '__main__':
    app.run()
