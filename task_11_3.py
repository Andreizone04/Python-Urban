import pprint

def introspection_info(obj):
    type_info = {'Тип': type(obj),
        'Атрибуты и Методы': obj.__dict__.keys() if hasattr(obj, '__dict__') else dir(obj),
        'Имя': obj.__name__ if hasattr(obj, '__name__') else 'Нет имени',
        'Модуль': obj.__module__ if hasattr(obj, '__module__') else 'Не модуль',
        'Документация': obj.__doc__,
        'Можно ли вызвать': callable(obj),
        'Идентификатор': id(obj),}
    return type_info


number_info = introspection_info(42)
pprint.pprint(number_info)
