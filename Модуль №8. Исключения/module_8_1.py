def add_everything_up(a, b):
    try:
        sum_ = a + b
        complete = f'{sum_}'

    except TypeError as exc:
        complete = f'{a}{b}'

    return complete


result = add_everything_up(123.456, 'строка')
print(result)
result = add_everything_up('яблоко', 4215)
print(result)
result = add_everything_up(123.456, 7)
print(result)
