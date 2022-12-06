# 6
'''Напишите функцию, которая принимает неограниченное количество числовых аргументов и возвращает кортеж из двух списков:
отрицательных значений (отсортирован по убыванию);
неотрицательных значений (отсортирован по возрастанию).
'''


def sortion(*arguments):
    negative_arguments = []
    positive_arguments = []
    for i in range(len(arguments)):
        if arguments[i] < 0:
            negative_arguments.append(arguments[i])
        else:
            positive_arguments.append(arguments[i])
    negative_arguments.sort(reverse=True)
    positive_arguments.sort()
    return (negative_arguments, positive_arguments)


print(sortion(2, 6, 9, -3, -7, -16, -1, -2, 1))

# 7
'''Строка называется палиндромом, если она пишется одинаково в обоих направлениях. Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah». Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом.
'''


def palindrom(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] == word[-i - 1]:
            answer = 'YES'
        else:
            answer = 'NO'
    return (answer)


print(palindrom('Анна'))

# 8
'''Вы загадываете число от 1 до 100 (включительно). Компьютер спрашивает у вас «Твое число равно, меньше или больше, чем число N?»,  где N — число, которое хочет проверить компьютер.
Вы отвечаете одним из трёх чисел:
1 — равно,
2 — больше,
3 — меньше.

Напишите программу, которая с помощью цепочки таких вопросов и ответов угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
'''
start = 1
finish = 101
count = 1
while True:
    n = (start + finish) // 2
    print('Загаданное число равно, меньше или больше', n)
    answer = int(input('1-равно, 2 - меньше, 3-больше'))
    if answer == 1:
        print('Я угадал!Ура! с', count, 'попытки')
        break
    elif answer == 2:
        finish = n
    elif answer == 3:
        start = n
    count += 1
print('Может повторим?')

# 10
'''Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года. Например, 10 июня 1960 года – магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определяющую, является ли введенная дата магической. Используйте написанную функцию в главной программе для отображения всех магических дат в XX веке.
'''


def magic_date(date):
    dictionary = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                  'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    data = int(date[0:2])
    key = (date[3:-5])
    month = dictionary.get(key)
    year = int(date[-2:])
    if data * month == year:
        answer = "YES, it's magic!"
    else:
        answer = 'No magic'
    return (answer)


print(magic_date(input()))
