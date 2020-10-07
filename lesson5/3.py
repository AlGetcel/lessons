# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
filename = '/home/alexander/work/salary.txt'
result = []
with open(filename, 'r') as file:
    salary = 0
    cou = 0
    fams = []
    for line in file:
        words = [i for i in line.strip().split(' ')]
        fam = words[0]
        sal = float(words[1])
        if sal < 20000.0:
            fams.append(fam)
        salary += sal
        cou += 1
print("Средняя зарплата составляет: {}".format(sal/cou))
print("Сотрудники с окладом меньше 20 тыс.: {}".format(fams))
