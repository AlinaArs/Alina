# 5
'''Необходимо реализовать калькулятор. Пользователь вводит строку из 3 элементов, разделенных пробелом -
ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2
Операнды - целые числа. Операции - арифметические (включая деление нацело и нахождение остатка)
Напишите программу, которая обрабатывает введенную пользователем строку и  вычисляет полученное действие.
Пропишите обработку возможных ошибок. Программа не должна завершаться при первой же ошибке, она должна предлагать
пользователю исправить ошибку и попробовать посчитать результат заново.
'''


def calculation(a, b, c):
    if b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    elif b == '*':
        print(a * c)
    elif b == '/':
        try:
            print(a / c)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

    elif b == '//':
        print(a // c)
    elif b == '%':
        print(a % c)
    elif b == '**':
        print(a ** c)
    else:
        print('Операция не определена, попробуйте еще раз')


a, b, c = int(input()), input(), int(input())
print(calculation(a, b, c))
