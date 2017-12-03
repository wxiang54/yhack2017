import sqlite3
from sqlite3 import Error
import os.path


PATH_TO_DB = "data/data.db"
db = sqlite3.connect(PATH_TO_DB)
c = db.cursor()


def setup_db():
    q = '''
CREATE TABLE ItemType (
    id integer NOT NULL CONSTRAINT ItemType_pk PRIMARY KEY,
    name varchar(50),
    est_fin_days double,
    catagories_id integer NOT NULL
);
'''
    c.execute(q)
    q = '''
CREATE TABLE Item (
   id integer NOT NULL CONSTRAINT Item_pk PRIMARY KEY,
   itemtype_id integer NOT NULL,
   exp_date date NOT NULL,
   qty integer
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
    q = ''' 
CREATE TABLE Catagory (
    id integer NOT NULL CONSTRAINT Catagories_pk PRIMARY KEY,
    name character(50)
);
'''
    c.execute(q)
    db.commit()

    
def addItem(itemName, exp_date, qty):
    q = "INSERT INTO Item(itemtype_id, exp_date, qty) VALUES (?, ?, ?);"
    c.execute(q, (getItemTypeID(itemName), exp_date, qty))
    db.commit()

#add item type
def createItem(catagoryName, itemName):
    q = "INSERT INTO ItemType(name, catagories_id) VALUES (?, ?);"
    c.execute(q, (itemName, getCatagoryID(catagoryName)))
    db.commit()

def createCatagory(name):
    q = "INSERT INTO Catagory(name) VALUES (?);"
    c.execute(q, (name,))
    db.commit()
    
def getCatagoryID(name):
    q = "SELECT id FROM Catagory WHERE name='%s';" % name
    return c.execute(q).fetchone()[0]

def getItemTypeID(name):
    q = "SELECT id FROM ItemType WHERE name='%s';" % name
    return c.execute(q).fetchone()[0]

#gets names only
def getAllCatagories():
    q = "SELECT name FROM Catagory ORDER BY name ASC;"
    return c.execute(q).fetchall()

def getAllItems():
    q = "SELECT name FROM Item ORDER BY name ASC;"
    return c.execute(q).fetchall()

if __name__ == "__main__":

    if c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Item';").fetchone():
        print 'db existed'
    else:
        setup_db()
        createCatagory("Food")
        createCatagory("Medicine")
        createItem("Food", "Lettuce")
        createItem("Food", "Tomato")
        createItem("Medicine", "Xans")
        createItem("Medicine", "Mol")
        addItem("Tomato", "2017-12-03", 5)
        addItem("Xans", "2018-02-02", 2)
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
