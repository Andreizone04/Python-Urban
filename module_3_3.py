def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [5, "Test", False]
print_params(*values_list)

values_dict = {'a': 10, 'b': 'Second', 'c': None}
print_params(**values_dict)

values_list_2 = [15, 'Done']
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
