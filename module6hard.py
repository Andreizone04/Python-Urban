class Figure:
    sides_count = 0

    def __init__(self, rgb, *side):
        self.__sides = list(side)
        self.__color = list(rgb)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *rgb):
        if rgb[0] >= 0 and rgb[0] <= 255 and rgb[1] >= 0 and rgb[1] <= 255 and rgb[2] >= 0 and rgb[2] <= 255:
            return True
        else:
            return False

    def set_color(self, *rgb):
        if self.__is_valid_color(*rgb):
            self.__color = rgb

    def __is_valid_sides(self, *sides):
        k = False
        if len(sides) == len(self.__sides):
            for i in sides:
                if i > 0 and isinstance(i, int):
                    k = True
                else:
                    k = False
                    return k
        return k
    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for i in self.__sides:
            p += i
        return p

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__radius = sides[0] / 3.14 * 2

    def get_square(self):
        s = 3.14 * (self.__radius ** 2)
        return s


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = 0
        for i in self.__sides:
            p += i
        p = p / 2
        return (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, sides):
        sides = [sides] * self.sides_count
        super().__init__(rgb, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится

print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())
