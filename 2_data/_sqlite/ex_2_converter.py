import json
import sqlite3


def adapt_json(data):
    return json.dumps(data)


def convert_json(raw):
    return json.loads(raw)


# error below
# conn = sqlite3.connect(":memory:")
# cur = conn.cursor()
#
# cur.execute('CREATE TABLE test(p json)')
#
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'pop': 10},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'pop': 20},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 3, 'pop': 30},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 4, 'pop': 40},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 5, 'pop': 50},))
# row = cur.fetchone()
#
# conn.close()

sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

cur.execute('CREATE TABLE test(p json)')
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'pop': 10},))
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'pop': 20},))
cur.execute('SELECT * FROM test')
record = cur.fetchone()
print(type(record[0]))
