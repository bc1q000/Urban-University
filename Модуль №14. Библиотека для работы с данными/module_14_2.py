import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()


cursor.execute('delete from Users where id = 6')
cursor.execute('select count(*) from Users')
total = cursor.fetchone()[0]
print(total)


cursor.execute('select sum(balance) from Users')
sum_ = cursor.fetchone()[0]
print(sum_)


cursor.execute('select avg(balance) from Users')
avg_ = cursor.fetchone()[0]
print(avg_)
print(sum_/total)


connection.commit()
connection.close()