import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
user TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (user, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}.gmail.com', i*10, 1000))
    if i % 2 == 1:
        cursor.execute('UPDATE Users SET balance = ? WHERE user = ?', (500, f'User{i}'))
    if i % 3 == 1:
        cursor.execute('DELETE FROM Users WHERE user = ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users WHERE age != 60')
hi = cursor.fetchall()
for i in hi:
    print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

connection.commit()
connection.close()
