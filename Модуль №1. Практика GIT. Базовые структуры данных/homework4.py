# homework4
my_string = input()
print(f'Количество символов введённого текста: {len(my_string)}\n'
      f'Строка в верхнем регистре: {my_string.upper()}\n'
      f'Строка в нижнем регистре: {my_string.lower()}\n'
      f'Удаление пробелов: {my_string.replace(' ', '')}\n'
      f'Первый символ строки: {my_string[0]}\n'
      f'Последний символ строки: {my_string[-1]}')
