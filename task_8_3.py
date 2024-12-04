class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __is_valid_vin(self, vin):
        k = False
        if isinstance(vin, int):
            k = True
        else:
            k = False
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if 1000000 <= vin <= 9999999:
            k = True
        else:
            k = False
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return k

    def __is_valid_numbers(self, numbers):
        k = False
        if isinstance(numbers, str):
            k = True
        else:
            k = False
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) == 6:
            k = True
        else:
            k = False
            raise IncorrectCarNumbers('Неверная длина номера')
        return k

    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            self.__vin = None
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            self.__numbers = None


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
