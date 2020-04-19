import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute(
    """CREATE TABLE "people_new" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name,
        last_name,
        birthday
    )"""
)
conn.execute("""INSERT INTO people_new(id, first_name, last_name, birthday)
                VALUES (1, "Bohdan", "Kalika", "15-03-1996"),
                        (2, "Nazar", "Kalika", "23-05-2002"),
                        (3, "Vitalik", "Ogorodnik", "23-11-1992")
""")
conn.row_factory = sqlite3.Row
users = conn.execute('SELECT * FROM "people_new"').fetchall()

user = users[0]
print(user.keys())
print(user['id'], user['iD'])
print(user['first_name'], user['first_NAME'], user['FIRST_NAME'])
