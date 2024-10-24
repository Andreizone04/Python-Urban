data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


def counter(i):
    scale_i = 0
    if type(i) == int:
        scale_i += i
    elif type(i) == str:
        scale_i += len(i)
    return scale_i


def calculate_structure_sum(object):
    scale = 0
    if type(object) == list:
        for i in object:
            if type(i) == list or type(i)== tuple or type(i) == dict:
                scale += calculate_structure_sum(i)
            else:
                scale += counter(i)
    if type(object) == tuple:
        for i in object:
            if type(i) == list or type(i)== tuple or type(i) == dict:
                scale += calculate_structure_sum(i)
            else:
                scale += counter(i)
    if type(object) == dict:
        for i,j in object:
            if type(i) == list or type(i)== tuple or type(i) == dict:
                scale += calculate_structure_sum(i)
            else:
                scale += counter(i) + counter(j)
    return scale


result = calculate_structure_sum(data_structure)

print(result)
