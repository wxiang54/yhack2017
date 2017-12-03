import sqlite3
from sqlite3 import Error
import os.path

PATH_TO_DB = "data/data.db"

def setup_db():
    db = sqlite3.connect(PATH_TO_DB)
    c = db.cursor()
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
    q = ''' CREATE TABLE Catagories (
    id integer NOT NULL CONSTRAINT Catagories_pk PRIMARY KEY,
    name character(50)
);
'''
    c.execute(q)
    db.commit()

    
if __name__ == '__main__':
    if not os.path.isfile("data.db"):
        setup_db()
