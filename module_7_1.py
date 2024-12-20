from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.file = ''

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        text = self.file.read()
        self.file.close()
        return text

    def add(self, *products):
        self.file = open(self.__file_name, 'r')
        product_list = list(products)
        file = self.file.read()
        self.file.close()
        self.file = open(self.__file_name, 'a')
        for product in product_list:
            if file.count(product.name) > 0:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                self.file.write(f'{product}\n')
        self.file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
