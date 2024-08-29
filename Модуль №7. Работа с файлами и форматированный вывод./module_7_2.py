def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'r+', encoding='utf-8') as file:
        for num, item in enumerate(strings):
            num_b = file.tell()

            line = num + 1

            file.writelines(f'{item}\n')
            strings_positions[(line, num_b)] = item

    return strings_positions


record = [f'Tell the text.',
          f'Использование кодировки utf-8',
          f'The file contains two languages',
          f'Благодарю!']

result = custom_write('module_7_2.txt', record)
print(result)
