import mysql.connector as mc
conn = mc.connect(host='localhost', user='Maram', password='M771234171m.', db='menagerie')
c = conn.cursor()


def show_female_dogs():
    c.execute('SELECT * FROM pet WHERE species = "dog" AND sex = "f"')
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    show_female_dogs()

if __name__ == '__main__':
    main()