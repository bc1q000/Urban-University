team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team2_time = 18015.2
tasks_total = score_2 + score_1
time_avg = 350.4

result_phrase = 'Результат битвы: выйграла команда'
result1 = f'"{result_phrase} {team1}!"'
result2 = f'"{result_phrase} {team2}!"'
challenge_result = result1 if score_1 > score_2 else result2

#  Использование %:
print('"В команде %s участников: %s' % (team1, team1_num) + '!"')
print('"Итого сегодня в командах участников: %(first)s и %(second)s' % {'second': team2_num, 'first': team1_num} + '!"')

#  Использование format():
print('"Команда {} решила задач: {}!"'.format(team2, score_2))
print('"{1} решили задачи за {0} с!"'.format(team2_time, team2))

#  Использование f-строк:
print(f'"Команды решили {score_1} и {score_2} задач".')
print(challenge_result)
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"')