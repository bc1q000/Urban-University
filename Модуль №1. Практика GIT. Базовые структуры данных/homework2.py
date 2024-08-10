# homework2
complete_tasks = 12
work_time = 1.5
title = 'Python'
print(f'Курс: {title}, всего задач: {complete_tasks}, затрачено часов {work_time}, '
      f'средее время выполнения {work_time / complete_tasks} часа.')



class Sentence():
    def __init__(self, complete_tasks, work_time, title):
        self.complete_tasks = complete_tasks
        self.work_time = work_time
        self.title = title

    def __str__(self):
        return (f'Курс: {self.title}, всего задач: {self.complete_tasks}, затрачено часов {self.work_time}, '
                f'средее время выполнения {self.work_time / self.complete_tasks} часа.')


f1 = Sentence(12, 1.5, 'Python')
print(f1)
