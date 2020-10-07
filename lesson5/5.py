# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from itertools import count

result = []
name = input('Задайте имя файла:')
dir_name = input('Введите директорию хранения:')
chis = int(input('Задайте границу:'))
full_name = dir_name + name

n = 1 
for i in count(chis):
    result.append(i)
    n += 1
    if n > 30:
        break

with open (full_name, 'w') as f:
    for i in result:
        f.write(str(i))
    f.close()
    
with open (full_name, 'r') as fl:
    for i in fl:
        num = [int(j) for j in i]
        print(sum(num))
