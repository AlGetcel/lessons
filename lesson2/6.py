# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

numbers = [i for i in input('Введите номера товаров:').split(' ')]
result = []
for i in numbers:
    print('Введите данные для товара номер:', i, end = '\n')
    a = input('Введите название товара:')
    b = input('Введите цену товара:')
    c = input('Введите количество товара:')
    d = input('Введите единицу измерения товара:')

    step = []

    d = {
         'название': a
        ,'цена:': b
        ,'количество:': c
        ,'ед:': d
    }
    step.append(i)
    step.append(d)
    step = tuple(step)
    result.append(step)

a, b, c, d = [], [], [], []

for i in result:
    for k, v in i[1].items():
        if k == 'название':
            a.append(v)
        elif k == 'цена:':
            b.append(v)
        elif k == 'количество:':
            c.append(v)
        elif k == 'ед:':
            d.append(v)

d1 = {
     'название': a
    ,'цена:': b
    ,'количество:': c
    ,'ед:': d
}
print(d1)