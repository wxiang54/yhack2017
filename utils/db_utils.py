import sqlite3
from sqlite3 import Error
import os.path

PATH_TO_DB = "data/data.db"
db = sqlite3.connect(PATH_TO_DB)
c = db.cursor()
if os.path.isfile("data.db"):
    setup_db()
    
def setup_db():
    q = '''
CREATE TABLE Item (
   id integer NOT NULL CONSTRAINT Item_pk PRIMARY KEY,
   name varchar(50),
   exp_date datetime NOT NULL,
   qty integer,
   est_fin_days double,
   catagories_id integer NOT NULL
);
'''
    c.execute(q)
    q = '''
CREATE TABLE List (
   id integer NOT NULL CONSTRAINT List_pk PRIMARY KEY,
   name varchar(50)
);
'''
    c.execute(q)
    q = '''
CREATE TABLE ListItem (
   id integer NOT NULL CONSTRAINT ListItem_pk PRIMARY KEY,
   list_id integer NOT NULL,
   item_id integer NOT NULL
);
'''
    c.execute(q)
    q = ''' CREATE TABLE Catagory (
    id integer NOT NULL CONSTRAINT Catagories_pk PRIMARY KEY,
    name character(50)
);
'''
    c.execute(q)
    db.commit()

def addItem(catagory, item):
    q = "INSERT INTO Item VALUES (?, ?);"
    c.execute(q, (getCatagoryId(catagory), getItemId(item)))
    db.commit()
    
def getCatagoryID(name):
    q = "SELECT id FROM Catagory WHERE name='?';"
    return c.execute(q, (name)).fetchone()[0]

def getItemID(name):
    q = "SELECT id FROM Item WHERE name='?';"
    return c.execute(q, (name)).fetchone()[0]

#gets names only
def getAllCatagories():
    q = "SELECT name FROM Catagory;"
    return c.execute(q).fetchall()

def getAllItems():
    q = "SELECT name FROM Item;"
    return c.execute(q).fetchall()

