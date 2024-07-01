# homework5
immutable_var = 1, 2.2, 'Python', True, [1, 2], (1, 2)
print(immutable_var)
# immutable_var[0] = 2
# print(immutable_var)  # Выдаст ошибку "TypeError: 'tuple' object does not support item assignment", так как кортеж - неизменяемый тип данных

print(immutable_var[4])     # Для проверки вывода элемента
immutable_var[4][0] = 5.5       # Беру 5 элемент "список" и изменяю внутри него int to float
print(immutable_var)
immutable_var[4][1] = 'Python'      # Так же список поддерживает множество изменяемых типов данных
print(immutable_var)
