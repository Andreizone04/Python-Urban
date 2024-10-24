data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(*object):
    counter = 0
    for i in object:
        if isinstance(i, int):
            counter += i
        if isinstance(i, str) and len(i) >= 1:
            counter += len(i)
        if isinstance(i, (list, tuple, set)):
            counter += calculate_structure_sum(*i)
        if isinstance(i, dict):
            counter += calculate_structure_sum(*i.keys())
            counter += calculate_structure_sum(*i.values())
    return counter


result = calculate_structure_sum(data_structure)

print(result)
