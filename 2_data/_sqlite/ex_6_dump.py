import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE "users" (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                birthday VARCHAR(30)
    )""")
conn.execute("""INSERT INTO users(id, first_name, last_name, birthday)
                VALUES(1, "Bohdan", "Kalika", "15-03-1996"),
                        (2, "Nazar", "Kalika", "23-05-2002")
""")

with open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)
        print('{}\n'.format(line))
