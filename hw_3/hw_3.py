# 1
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a = a + b
print('Кол-во цифр 5 при первом объединении: ', a.count(5))
for i in a:
    if i == 5:
        a.remove(i)
a = a + c
print('Кол-во цифр 3 при втором объединении:', a.count(3))
print(a)

# 2
first_class = []
for i in range(160, 177, 2):
    first_class.append(i)
second_class = []
for i in range(162, 181, 3):
    second_class.append(i)
united_class = first_class + second_class
print('Отсортированный список учеников:', sorted(united_class))

# 4
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print('Сейчас на вечеринке 5 человек:', guests)
answer = input('Гость пришёл или ушёл?').lower()
while answer != 'пора спать':
    if answer == 'пришел' and len(guests) < 6:
        name = input('Имя гостя:')
        print('Привет, {}!'.format(name))
        guests.append(name)
    elif answer == 'пришел' and len(guests) == 6:
        name = input('Имя гостя:')
        print('Прости, {}, но мест нет.'.format(name))
    elif answer == 'ушел':
        name = input('Имя гостя:')
        print('Пока, {}!'.format(name))
        guests.remove(name)
    print('Сейчас на вечеринке {} человек:'.format(len(guests)), guests)
    answer = input('Гость пришёл или ушёл?').lower()
else:
    print('Вечеринка закончилась, все легли спать.')

# 5
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
violator_songs_dict = dict(violator_songs)
numbers = int(input('Сколько песен выбрать?'))
lst = []
for i in range(numbers):
    music = input('Название {}-й песни:'.format(i + 1))
    if music in violator_songs_dict.keys():
        lst.append(violator_songs_dict[music])
    else:
        break
print(round(sum(lst), 2))

# 6
first_lst = []
second_lst = []
for i in range(3):
    first_lst.append(int(input('Введите {}-е число для первого списка:'.format(i + 1))))

for i in range(7):
    second_lst.append(int(input('Введите {}-е число для второго списка:'.format(i + 1))))
print('Первый список:', first_lst)
print('Второй список:', second_lst)
first_lst = first_lst + second_lst
uniq_first_list = list(set(first_lst))
print('Новый первый список с уникальными элементами:', uniq_first_list)
