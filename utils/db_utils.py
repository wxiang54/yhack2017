import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


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

CREATE TABLE List (
   id integer NOT NULL CONSTRAINT List_pk PRIMARY KEY,
   name varchar(50)
);

CREATE TABLE ListItem (
   id integer NOT NULL CONSTRAINT ListItem_pk PRIMARY KEY,
   list_id integer NOT NULL,
   item_id integer NOT NULL
);

CREATE TABLE Catagories (
   id integer NOT NULL CONSTRAINT Catagories_pk PRIMARY KEY,
   name character(50)
);
    '''
        
if __name__ == '__main__':
    create_connection("items.db")
