import sqlite3
import sys


def query_pets():
    sqlite_file = 'pets'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    required_id = input("Gimme ID:\n")
    person = c.execute("SELECT * FROM person WHERE id={}".format(required_id)).fetchone()
    if not person:
        sys.exit("check you person ID pls")
    else:
        doggo = c.execute("SELECT * FROM person_pet WHERE person_id={}".format(
            person[0])).fetchall()
        for e in doggo:
            owner = c.execute("SELECT * FROM pet WHERE id={}".format(e[1])).fetchall()
            for i in owner:
                print("{} {}, {} years old and owned {}, a {}, that was {} years old".format(
                        person[1], person[2], person[3], i[1], i[2], i[3]))


if __name__ == '__main__':
    query_pets()
