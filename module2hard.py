import random


def password():
    for i in range(1, 21):                    # 1й элемент i - наименьший
        for j in range(i + 1, 21):            # 2й элемент не равный i и больше него на 1
            if stone_slot[0] % (i + j) == 0:  # проверка делителя
                a = f'{i}{j}'
                stone_slot[1].append(a)       # добавление пары в список
    print(stone_slot[0], ':', sep='', end=' ')
    for item in stone_slot[1]:
        print(item, end='')

stone_slot = ['*', []]                        # Две каменные вставки для чисел. 2я - обязательно "список"
stone_slot[0] = random.randint(3, 20)   # Изменение 1-го слота

password()
