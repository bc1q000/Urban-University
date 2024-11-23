#1st program
print('1st:', 9 ** 0.5 * 5)

#2st program
print('2st:', 9.99 > 9.98 and 1000 != 1000.1)

#3st program OLD
a = 1234
b = 5678
print('3st old:', (a // 10) % 100 + (b // 10) % 100)

# 3st program new
print('3st new:')
a = 2 * 2 + 2
print(a)
b = 2 * (2 + 2)
print(b)
print(a == b)

#4st program OLD
a = 13.42
b = 42.13
print('4st old:', a // 1 == b * 100 % 100 or b // 1 == a * 100 % 100)

#4st program new
string = '123.456'
print('4st new:', string[4])