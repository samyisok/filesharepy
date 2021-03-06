import sqlite3
import os
import random


class MainDb():
    def exsql(self, query):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def isSQLite3(self, filename):
        from os.path import isfile, getsize

        if not isfile(filename):
            return False
        if getsize(filename) < 100: # SQLite database file header is 100 bytes
            return False
        else:
            fd = open(filename, 'rb')
            Header = fd.read(100)
            fd.close()

            if Header[0:16] == 'SQLite format 3\000':
                return True
            else:
                return False

    def init_exist_db(self):
        if self.isSQLite3(self.db_name):
            pass
        else:
            query = """create table files (
                     id integer primary key autoincrement,
                     name text,
                     path text,
                     webpath text
                     );
                     """
            self.exsql(query)


    def __init__(self, db_name):
        self.db_name = db_name
        self.read_db_query = 'select * from files;'
        self.init_exist_db()


    def read_db(self, row=None):
        if row is None:
            return self.exsql(self.read_db_query)
        else:
            query = "select {0} from files".format(row)
            return self.exsql(query)


    def insert_files(self, name, path, webpath):
        query_tmp = "INSERT INTO files (name, path, webpath) VALUES ('{0}', '{1}', '{2}')".format(name, path, webpath)
        print query_tmp
        self.exsql(query_tmp)



