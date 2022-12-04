# 7
skates_number = int(input('Кол-во коньков:'))
skates_size = []
for i in range(skates_number):
    skates_size.append(input('Размер {}-й пары:'.format(i + 1)))
people_number = int(input('Кол-во людей:'))
people_size = []
for i in range(people_number):
    people_size.append(input('Размер ноги {}-го человека:'.format(i + 1)))
counter = 0
for i in range(len(people_size)):
    for j in range(len(skates_size)):
        if people_size[i] <= skates_size[j]:
            counter += 1
            del skates_size[j]
            break
print(counter)

# 8
people = int(input('Кол-во человек: '))
dropped = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', dropped, 'человек')
people_list = list(range(1, people + 1))
out = 0

for _ in range(people - 1):
    print('Текущий круг людей', people_list)
    start_count = out % len(people_list)
    out = (start_count + dropped - 1) % len(people_list)
    print('Начало счёта с номера', people_list[start_count])
    print('Выбывает человек под номером', people_list[out])
    people_list.remove(people_list[out])

print('Остался человек под номером', *people_list)

# 4.2.15
quantity_cargo = int(input('Количество предметов?'))
weight_cargo = []
for i in range(quantity_cargo):
    weight = int(input('Какой вес предмета?'))
    weight_cargo.append(weight)
car_capacity = int(input('Грузоподъемноость грузовика?'))
sum_cargo = sum(weight_cargo)
if sum_cargo > car_capacity:
    print('Перевозка невозможна')
else:
    print('Поехали!')

# 4.2.8
n = int(input())
lst = [0, 5, 10, 15, 20, 25]
for i in range(len(lst)):
    if lst[i] <= n:
        print(lst[i])

# 4.2.19
a, b, c = int(input()), int(input()), int(input())
for i in range(a, b + 1):
    if i % c == 0:
        print(i, end=' ')

# 4.2.25
num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print('{} * {} ='.format(i, j), i * j, end ='\n')

