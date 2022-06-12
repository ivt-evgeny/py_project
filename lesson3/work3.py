# Задание 1 -------------------------------------------------------

def div(*args):
    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "на ноль делить нельзя"
    return res

print(f'Результат: {div()}')



# Задание 2 ---------------------------------------------------------

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname='Питонов', name='Питон', year='1991', city='MSK', email='python@ya.ru', telephone='89013056111'))



# Задание 3 ---------------------------------------------------------

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат - {my_func(int(input("Первый аргумент: ")), int(input("Второй аргумент: ")), int(input("Третий аргумент: ")))}')



# Задание 4 ---------------------------------------------------------

def my_func(x, y):
    return x ** y
print(my_func(2, -5))



# Задание 5 ---------------------------------------------------------

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма составляет {sum_res}')
    print(f'Ваша окончательная сумма составляет {sum_res}')

my_sum()



# Задание 6 ---------------------------------------------------------

def int_func (*args):
    word = input("Введите слово: ")
    print(word.title())
    return
int_func()
