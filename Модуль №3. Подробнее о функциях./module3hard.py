# Дополнительное практическое задание по модулю module3hard.py


def calculate_structure_sum(data):  # Рекурсивная функция для подсчета ссуммы
    total_sum = 0

    def helper(item):  # Рекурсивная функция для проверки классов объектов
        nonlocal total_sum  # Берется локальная переменная из def calculate_structure_sum
        if isinstance(item, (int, float)):  # Проверка на число
            total_sum += item
        elif isinstance(item, str):  # Проверка на строку
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Проверка на виды списков
            for element in item:
                helper(element)
        elif isinstance(item, dict):  # Словарь - отдельный вид искусства
            for key, value in item.items():
                helper(key)
                helper(value)

    helper(data)
    return total_sum

# Входные данные в переменной
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
