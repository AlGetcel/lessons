# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
# При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к 
# полученной ранее сумме и после этого завершить программу.
def calculate():
    result = 0
    failed = []

    while True:
        str_numbers = [i for i in input('Введите числа').split(' ')]
        if input('Введите Enter для подсчета суммы') == 'A':
            for i in str_numbers:
                if i.isdigit():
                    result += int(i)
                else:
                    failed.append(i)
            if failed:
                return result
        print(result)
    
calculate()