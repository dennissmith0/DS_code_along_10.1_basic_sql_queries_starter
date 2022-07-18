import sqlite3
import queries as q

conn = sqlite3.connect('chinook.db')

curs = conn.cursor()

data = [
    ('New York', 'NY', 8, 1, 1),
    ('Los Angeles', 'CA', 11, 0, 1),
    ('Seattle', 'WA', 7, 1, 0),
    ('San Francisco', 'CA', 5, 0, 0)
]

if __name__ == '__main__':
    pass
