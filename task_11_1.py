import subprocess
import sys

# """
# вызывается один раз в остальные запуски рекомендую закоментировать
packages = ['pandas', 'xlrd', 'numpy']
for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
# """
import pandas as pd
import numpy as np

test_file = pd.read_excel("test.xls")

print(f'последние 3 строчки с начала \n {test_file.head(3)}')
print(f'последние 3 строчки с конца \n {test_file.tail(3)}')

test_array = np.array(test_file)  # конвертация в списки

max_list = [max(x) for x in test_array]
min_list = [min(x) for x in test_array]

print(f'максимальное значение в таблице : {max(max_list)}')
print(f'минимальное значение в таблице : {min(min_list)}')
