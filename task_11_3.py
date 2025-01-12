import pprint

def introspection_info(obj):
    type_info = {'Тип':type(obj),'атрибуты и методы объекта':dir(obj)}
    return type_info


number_info = introspection_info(42)
pprint.pprint(number_info)
