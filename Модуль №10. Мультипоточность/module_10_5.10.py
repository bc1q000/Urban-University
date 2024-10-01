import datetime
import multiprocessing


def files_names():
    """Возвращает сиаисок всех имен файлов"""
    file_names = [f'file {num}.txt' for num in range(1, 5)]
    return file_names


def read_info(file_name):
    """Функция чтения информации из файла построчно"""
    start = datetime.datetime.now()

    all_data = []

    try:
        with open(file_name, 'rt') as file:
            for line in file:
                if line != '':
                    all_data.append(line)
                else:
                    break
            # data = file.readlines()
            # print(all_data)
    except FileNotFoundError:
        print(f'Файла {file_name} не существует')

    end = datetime.datetime.now()
    time_res = end - start
    print(f'Время обаботки {file_name}: {time_res}')
    return all_data


if __name__ == '__main__':
    # Линейный вызов
    print('Линейная обработка файлов')
    start = datetime.datetime.now()

    for file in files_names():
        read_info(file)

    end = datetime.datetime.now()
    time_res = end - start
    print(f'Итоговое время работы линейной работы программы: {time_res}\n')
    # print(all_data)

    # Мультипроцессорный вызов
    print('Мультипроцессорная обработка файлов')
    start = datetime.datetime.now()

    processes = [multiprocessing.Process(target=read_info, args=[filename]) for filename in files_names()]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    end = datetime.datetime.now()
    time_res = end - start
    print(f'Итоговое время работы мультипроцессорной работы программы: {time_res}\n')
