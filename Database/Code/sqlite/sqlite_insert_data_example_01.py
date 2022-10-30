import sqlite3

connection = sqlite3.connect("Movies.db")
cursor = connection.cursor()

# cursor.execute('''INSERT INTO Movies VALUES
#                ('Taxi driver','Lim Ah Teck', 1965)''')

# cursor.execute('''SELECT * FROM Movies''')

# famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
#                 ('Back to the Future', 'Steven Spilberg', 1985),
#                ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)
# records = cursor.execute('''SELECT * FROM Movies''')

# print(cursor.fetchone())

# # More than one records
# print(cursor.fetchall())

# for record in records:
#     print(record)

release_year = (1985,)
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

connection.commit()
connection.close()
