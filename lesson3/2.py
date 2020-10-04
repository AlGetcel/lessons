# 2. Реализовать функцию, принимающую несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.
name, surname, birthday, city, email, t_number = 'alex', 'get', '10.01.1901', 'msk','aagetc@gm', '05-05-05'
def func_man(name, surname, birthday, city, email, t_number):
    return name, surname, birthday, city, email, t_number

func_man(name, surname, birthday, city, email, t_number)
