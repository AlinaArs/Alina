# 1
def max_common_divisor(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def min_common_divisor(a, b):
    return (a * b) / max_common_divisor(a, b)


a = 20
b = 6
nok = int(min_common_divisor(a, b))
print("Наименьшее общее кратное {} и {} равно {}".format(a, b, nok))
print("Наибольший общий делитель {} b {} равно {}".format(a, b, max_common_divisor(a, b)))

# 2
'''Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.'''


def number_in_sentence(n):
    counter = 0
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in range(len(n)):
            if n[i] in number:
                counter += 1
    return counter

print(number_in_sentence('Моей милой всего 25. И красивее нее не сыскать. Моей милой всего 25.'))

# 3
'''Дана строка s и символ k. Реализуйте функцию, рисующую рамку из символа k вокруг данной строки, например:

**************
*Текст в рамке*
**************
'''


def str_sym(s, k):
    first_and_third_str = k * (len(s) + 2)
    second_str = k + s + k
    return (first_and_third_str, second_str, first_and_third_str)


result = list(str_sym('World', '?'))
print(*result, sep='\n')

# 4
'''Упражнение 4.
Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается.

'''


def statistics(sentence):
    sentence = sentence.lower()
    sentence_lst = list(sentence)
    sentence_uniq = set(sentence)
    dictionary = dict()
    for i in range(len(sentence_uniq)):
        quantity = sentence_lst.count(sentence_lst[i])
        dictionary[sentence[i]] = quantity
    return dictionary


print(statistics('И лампа не горит И врут календари'))


# 5
'''Используя шифр Цезаря (достаточно только букв русского алфавита, знаки препинания не изменяются), зашифруйте, а затем расшифруйте введенную строку.
'''


def message(initial_message):
    initial_message = initial_message.upper()
    k = 3
    lst_new_message = []
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    for i in range(len(initial_message)):
        if initial_message[i] in alphabet:
            new_letter = alphabet[alphabet.index(initial_message[i]) + 3]
            lst_new_message.append(new_letter)
        else:
            lst_new_message.append(initial_message[i])
    new_message = str(lst_new_message)
    return (new_message)


print(message('Пошел есть'))


