# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.
filename = '/home/alexander/work/lesson5.txt'
filename1 = '/home/alexander/work/lesson5_replaced.txt'
dic = {
    'One': 'Один'
    ,'Two': 'Два'
    ,'Three': 'Три'
    ,'Four': 'Четыре'
}
result = []
with open(filename, 'r') as file:
    for line in file:
        words = [i for i in line.strip().split(' ')]
        words[0] = dic[words[0]]
        result.append(words)
file.close()

with open(filename1, 'w') as f:
    for i in result:        
        f.write(str(i) + '\n')
f.close()
