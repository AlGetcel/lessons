# 1. Создать программно файл в текстовом формате, записать в него построчно данные, 
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
result = []
name = input('Задайте имя файла:')
dir_name = input('Введите директорию хранения:')
full_name = dir_name + name

while True:
    row = input('Введите данные: ')
    if row == '':
        break
    else:
        result.append(row)
        
with open(full_name, 'w') as f:
    for i in result:
        f.write(str(i) + '\n')
f.close()
