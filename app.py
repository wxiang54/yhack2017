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

@app.route('/add-new/')
def add_new():
    cat = db_utils.getAllCategories()
    return render_template('addnew.html', categories = cat)

@app.route('/add-category/', methods=["GET", "POST"])
def add_category():
    if request.method == "GET":
        return render_template("add-category.html")
    cat_name = request.form.get("cat_name")
    if not cat_name:
        return redirect( url_for("add_category") )

    db_utils.createCategory(request.form.get("cat_name"))
    return redirect( url_for("items") )

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
    db_utils.setup_db()
