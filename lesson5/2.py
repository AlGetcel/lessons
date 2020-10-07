# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
# количества слов в каждой строке.
filename = '/home/alexander/work/lesson5.txt'
result = []
with open(filename, 'r') as file:
    cou = 0
    for line in file:
        words = [i for i in line.strip().split(' ')]
        print("Количество слов в строке {} = {}".format(1 if cou ==0 else cou + 1 , len(words)))
        cou += 1
print("Количество строк в файле = {}".format(cou))
