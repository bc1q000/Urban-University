# Способы вызова функции module_3_2.py


def send_email(massege, recipient, sender = 'university.help@gmail.com'):
    list_domens = ['.ru', '.com', '.net']
    count = 0
    if sender != recipient:
        if '@' in recipient and '@' in sender:
            for i in range(len(list_domens)):
                for j in range(len(list_domens)):
                    if list_domens[i] in recipient:
                        count += 1
                        break
                    else:
                        count += 0
                if list_domens[i] in sender:
                    count += 1
                    break
                else:
                    count += 0
            if count == 2:
                if sender == 'university.help@gmail.com':
                    print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
                else:
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')
            else:
                print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        else:
            print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    else:
        print('Нельзя отправить письмо самому себе!')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')