from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    strings_list = list(strings)
    file = open(file_name, 'w', encoding='utf-8')
    i = 0
    for string in strings_list:
        i += 1
        byte = file.tell()
        strings_positions[(i, byte)] = string
        file.write(f'{string}\n')
    return strings_positions


info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
