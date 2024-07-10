numbers = [n for n in range(1, 16)]  # Генерация списка из последовательных чисел
primes = []
not_primes = []
for i in numbers:
    if i == 2 or i == 3 or i == 5:  # Отсекаем простые числа, которые равны делителям составных
        primes.append(i)
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0:  # Делители составных чисел
        not_primes.append(i)
    elif i == 1:  # Пропускаем единицу, так как она не относится ко множеству простых и составных чисел
        pass
    else:
        primes.append(i)  # Запись простых чисел
print(f'Primes: {primes}\n'
      f'Not Primes: {not_primes}')

