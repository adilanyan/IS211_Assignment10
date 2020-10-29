import sqlite3


def insert_data():
    sqlite_file = '/Users/yuripetrovsky/Desktop/study/IS211/IS211_Assignment10/pets'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    list = [{"Person": (1, "James", "Smith", 41)},
            {"Person": (2, 'Diana', 'Greene', 23)},
            {"Person": (3, 'Sara', 'White', 27)},
            {"Person": (4, 'William', 'Gibson', 23)},
            {"Pet": (1, 'Rusty', 'Dalmation', 4, 1)},
            {"Pet": (2, 'Bella', 'AlaskanMalamute', 3, 0)},
            {"Pet": (3, 'Max', 'CockerSpaniel', 1, 0)},
            {"Pet": (4, 'Rocky', 'Beagle', 7, 0)},
            {"Pet": (5, 'Rufus', 'CockerSpaniel', 1, 0)},
            {"Pet": (6, 'Spot', 'Bloodhound', 2, 1)},
            {"Person_Pet": (1, 1)}, {"Person_Pet": (1, 2)},
            {"Person_Pet": (2, 3)}, {"Person_Pet": (2, 4)},
            {"Person_Pet": (3, 5)}, {"Person_Pet": (4, 6)}
            ]
    for i in list:
        for key, value in i.items():
            if key == "Person":
                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?)".format(key),
                          (value[0], value[1], value[2], value[3]))
            if key == "Pet":
                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?)".format(key),
                          (value[0], value[1], value[2], value[3], value[4]))
            if key == "Person_Pet":
                c.execute("INSERT INTO {} VALUES(?, ?)".format(key),
                          (value[0], value[1]))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_data()
