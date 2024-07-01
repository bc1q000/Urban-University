# homework5

# КОРТЕЖИ
immutable_var = 1, 2.2, 'Python', True, [1, 2], (1, 2)
print(immutable_var)
# immutable_var[0] = 2
# print(immutable_var)  # Выдаст ошибку "TypeError: 'tuple' object does not support item assignment", так как кортеж - неизменяемый тип данных

print(immutable_var[4])     # Для проверки вывода элемента
immutable_var[4][0] = 5.5       # Беру 5 элемент "список" и изменяю внутри него int to float
print(immutable_var)
immutable_var[4][1] = 'Python'      # Так же список поддерживает множество изменяемых типов данных
print(immutable_var)


# СПИСКИ
mutable_list = immutable_var[4]
print(mutable_list)
mutable_list.append(True)   # Поддерживает добавление лишь одного аргумента
mutable_list.extend(['Urban', 4])
print(mutable_list)

mutable_list.append(['список в список?', 4])
print(mutable_list)
print(type(mutable_list[5]))    # Есть ли практическое применение этому?