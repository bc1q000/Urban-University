first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = []
for x, y in zip(first, second):
    if len(x) != len(y):
        first_result.append(len(x) - len(y))
print(first_result)

for x in range(len(first)):
    for y in range(len(second)):
        if x == y:
            if len(first[x]) != len(second[y]):
                print(f'Длина {first[x]} ({len(first[x])}), '
                      f'а длина {second[y]} ({len(second[y])}): {len(first[x]) - len(second[y])}')
