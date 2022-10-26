import math

# 1
number = int(input())
sum = (number * (number + 1)) / 2
print(int(sum))

# 2
a, b = int(input()), int(input())
print(a + b, a - b, a * b, round(a / b, 2), a % b, a ** b, round(math.log10(a), 2))
print(a < b, a <= b, a > b, a >= b, a != b, a == b, sep='\n')

# 3
x, y, z = int(input()), int(input()), int(input())
print(round((((x ** 5 + 7) / abs(-6) * y) ** 1 / 3) / (7 - (z % y)), 3))

# 4
R1, R2 = int(input()), int(input())
print(float(R1 + R2))

# 5
a5, b5, m, n = int(input()), int(input()), int(input()), int(input())
x5 = -b / a
if m <= x5 <= n:
    print('х5 попадает в отрезок [m;n]')
else:
    print('x5 не попадает в отрезок [m;n]')

# 6
v, t = int(input()), int(input())
s = v * t
km = 0
if s > 122:
    km = s % 122
else:
    km = s
print(km)

# 7
num1, num2 = int(input()), int(input())
n1num1 = num1 // 10
n2num1 = num1 % 10
n1num2 = num2 // 100
n3num2 = num2 % 100
n2num2 = (num2 // 10) % 10
print(n1num1 + n2num1, n1num1 * n2num1)
print(n1num2 + n2num2 + n3num2, n1num2 * n2num2 * n3num2)

# 8
lst = list()
lst.append(input())
lst.append(input())
lst.append(input())
lst.sort()
print(*lst)
print('min =', min(lst), 'max =', max(lst))

# 9
a9 = int(input('Введите первое число: '))
b9 = int(input('Введите второе число: '))
print(a9, b9)
lst = [b9, a9]
a9 = lst[0]
b9 = lst[1]
print(a9, b9)
