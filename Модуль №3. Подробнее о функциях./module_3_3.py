# Распаковка позиционных параметров module_3_3.py

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [10, 'слово', True]
values_dict = {'a': 3, 'b': 2, 'c': 1}
values_list_2 = [False, 1.01234]

# 1. Функция с параметрами по умолчанию
print_params()  # Выводит заданные параметры
print_params(a = True, b = 25, c = 'строка')  # Изменяет параметры и выводит из без проблем
print_params(c = [1, 2, 3])  #

# 2. Распаковка параметров
print_params(*values_list)  # Распаковка выполняется и на заданные параметры
print_params(*values_dict)  # с одной * распаковываются ключи
print_params(**values_dict)  # с двумя ** распаковываются элементы словаря

# 3. Распаковка + отдельные параметры
print_params(*values_list_2,)  # Изменяются первые два параметра
print_params(*values_list_2, 42)  # 42 подставляется в параметр С
print_params(42, *values_list_2)  # 42 подставляется в параметр А
