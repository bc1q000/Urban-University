# Пространство имён module_3_1.py
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    cortege = (len(string), string.upper(), string.lower())
    print(cortege)
    count_calls()


def is_contains(string, list_to_search):
    init = False
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower():
            init = True
        else:
            init = False
    print(init)
    count_calls()


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])  # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic'])  # No matches
print(calls, '\n')   #[4]

string_info('Пространство имён')
string_info('начаЛьные ЗНАНИЯ о пространстве имЁн')
is_contains('Вызовы', ['зов', 'Зовут', 'выЗОВЫ'])  # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic'])  # No matches
print(calls)  #[8]
