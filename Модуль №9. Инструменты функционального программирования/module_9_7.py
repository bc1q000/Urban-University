def decorator(func):
    def is_prime(*args, **kwargs):
        result = func(*args)

        for num in range(1, result + 1):
            count_dell = 0

            for dell in range(1, num + 1):
                if num % dell == 0:
                    count_dell += 1
            if count_dell == 2:
                prime = 'Простое'
            else:
                prime = 'Составное'


        return prime, result
    return is_prime

@decorator
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

a = sum_three(9, 1, 1)
print(a)