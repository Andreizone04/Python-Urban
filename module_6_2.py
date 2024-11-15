class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f'Модель {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя {self.__engine_power}'

    def get_color(self):
        return f'Цвет {self.__color}'

    def print_info(self):
        print(f'Модель {self.__model}')
        print(f'Мощность двигателя {self.__engine_power}')
        print(f'Цвет {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if self.__COLOR_VARIANTS.count(new_color.lower()) >= 1:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
        __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()
