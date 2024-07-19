# Способы вызова функции module_3_2.py


def send_email(massege, recipient, sender='university.help@gmail.com'):
    list_domens = ['.ru', '.com', '.net']  # Список локальных доменов, разрешенных к использованию.
    count = 0  # Переменная, для проверки доменов у адресов.

    '''начинаем проверку с самого редкого события, так как программа содержит много условий'''

    if sender != recipient:  # 1. Самое редкое, идем дальше при выполнении.
        if '@' in recipient and '@' in sender:  # 2. Второе по редкости. Иногда можно забыть про знак @. Идем дальше при выполнении.
            for i in range(len(list_domens)):  # 2.1 Цикл, осуществляющий проверку домена sender.
                for j in range(len(list_domens)):  # 2.2 Цикл, осуществляющий проверку домена recipient.
                    if list_domens[i] in recipient:
                        count += 1
                        break  # 2.2 При нахождении прерываем
                    else:
                        count += 0
                if list_domens[i] in sender:
                    count += 1
                    break  # 2.1 При нахождении прерываем
                else:
                    count += 0
            if count == 2:  # 3. И, если уж так совпало, что все правильно, и все есть, идем дальше.
                if sender == 'university.help@gmail.com':  # 4. Проверяем на стандартный адрес.
                    print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
                else:  # 4. В ином случае уже НЕСТАНДАРТНЫЙ.
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')
            else:
                print(
                    f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')  # 3. Если разрешенного домена нет хотя бы в одном адресе
        else:
            print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')  # 2. Если не выполняется.
    else:
        print('Нельзя отправить письмо самому себе!')  # 1. Если не выполняется.


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
