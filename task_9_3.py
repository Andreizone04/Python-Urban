first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) != len(j))

second_result = (bool(len(first[i]) - len(second[i])==0)  for i in range(len(first)))

print(list(first_result))

print(list(second_result))
