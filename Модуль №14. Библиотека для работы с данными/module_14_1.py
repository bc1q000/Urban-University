import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )'''
)

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

 for i in range(10):
     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i+1}', f'ex{i+1}@ya.ru', f'{(i+1)*10}', f'1000'))



 for i in range(0, 11, 2):
     cursor.execute(f'UPDATE Users SET balance = ? WHERE id = {i+1}', (500,))

 for i in range(0, 11, 3):
     cursor.execute(f'DELETE FROM Users WHERE id = {i+1}')



cursor.execute('SELECT username, email, age, balance FROM Users WHERE AGE != 60')
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()