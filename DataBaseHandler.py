import sqlite3

class DataBaseHandler() :

     DB_NAME = 'database.db'

     @staticmethod
     def get_connection():
         return sqlite3.connect(DataBaseHandler.DB_NAME)

     @staticmethod
     def create_table():

         with DataBaseHandler.get_connection() as conn :
            conn.execute(''' CREATE TABLE IF NOT EXISTS students(
                          id_student INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          email TEXT NOT NULL,
                          gender TEXT NOT NULL);
            ''')

     @staticmethod
     def insert_student(name,email,gender):
         with DataBaseHandler.get_connection() as conn :
             conn.execute(
                 ''' INSERT INTO students (name,email,gender) VALUES (?,?,?);
                 ''',(name,email,gender)
             )

     @staticmethod
     def get_all_students():
         with DataBaseHandler.get_connection() as conn :
              return conn.execute('SELECT * FROM students ;').fetchall()


DataBaseHandler.create_table()