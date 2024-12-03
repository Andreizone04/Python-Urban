def personal_sum(numbers):
    a = {'result': 0, 'incorrect_data': 0}
    for i in numbers:
        try:
            a['result'] += i
        except TypeError:
            a['incorrect_data'] += 1
    return a


def calculate_average(numbers):
    a = 0
    try:
        for i in numbers:
            try:
                a = a + i
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    answer = personal_sum(numbers)
    try:
        b = answer['result'] / (len(numbers) - answer['incorrect_data'])
    except ZeroDivisionError:
        b = 0
    return b

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
