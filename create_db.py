# read_database.py

import mysql.connector as mc

conn= mc.connect(host='localhost',user='Maram',password='M771234171m.',db='menagerie')
c = conn.cursor()

def creat_db():
    c.execute('CREATE DATABASE menagerie')
    writers = c.fetchall() # data is read in the form of list
    for writer in writers: # print individual item in the list
        print(writer) # data at each row is saved as tuple
def main():
    creat_db()

if __name__ == '__main__':
    main()