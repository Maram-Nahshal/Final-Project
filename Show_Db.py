import mysql.connector as mc

conn= mc.connect(host='localhost',user='Maram',password='M771234171m.',db='menagerie')
c = conn.cursor()
def show_data():
    c.execute("show databases")
    databases = c.fetchall() # data is read in the form of list
    for show in databases: # print individual item in the list
        print(show) # data at each row is saved as tuple
def main():
    show_data()

if __name__ == '__main__':
    main()