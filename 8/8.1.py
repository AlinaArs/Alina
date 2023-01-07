# 1
'''На вход подается файл input_numbers.txt, где записано N целых чисел, которые могут быть разделены пробелами и
концами строк. Напишите программу, которая выводит сумму чисел в выходной файл output_sum.txt
'''
filenam = "input_numbers.txt"
with open(filenam, encoding="utf-8") as fh:
    data = fh.read()
    d_list =(data.split())
    data_list = []
    for i in range(len(d_list)):
        data_list.append(int(d_list[i]))
filename_2 = "output_sum.txt"
with open(filename_2, "w", encoding="utf-8") as fh_2:
    fh_2.write(str(sum(data_list)))


# 2
'''Как вы знаете, в языке Python для создания комментариев в коде используется символ #. Комментарий начинается с 
этого символа и продолжается до конца строки – без возможности остановить его раньше. В данном упражнении вам предстоит 
написать программу, которая будет удалять все комментарии из исходного файла с кодом на языке Python. Пройдите по всем 
строкам в файле на предмет поиска символа #. Обнаружив его, программа должна удалить все содержимое, начиная с этого 
символа и до конца строки. Для простоты не будем рассматривать ситуации, когда знак решетки встречается в середине 
строки. Сохраните новое содержимое в созданном файле. Имена файла источника и файла назначения должны быть запрошены 
у пользователя. Удостоверьтесь в том, что программа корректно обрабатывает возможные ошибки при работе с обоими файлами.
'''

file = input("Введите имя файла Python: ")
try:
    inf = open(file, "r")
except:
    print("При открытии файла возникла проблема.")
    inf.close()

outf = input("Введите имя нового файла: ")
try:
    outf = open(final_file, "w")
except:
    print("С создаваемым файлом возникла проблема.")
    outf.close()

try:
    for line in inf:
        pos = line.find("#")
    if pos > –1:
`       line = line[0 : pos]
        line = line + "\n"
        outf.write(line)
    inf.close()
    outf.close()
except:
    print("При обработке файла возникла проблема.")
    inf.close()
    outf.close()

# 3
'''Реализуйте модернизированную версию контекст менеджера File - теперь, при попытке открыть несуществующий файл, менеджер
 автоматически создаёт и открывает этот файл в режиме записи. На выходе из менеджера подавляются все исключения, 
 связанные с файлами.

'''
class File:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)  # Add self.mode
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':
    with File('example.txt', 'w') as file:
        file.write('Hello World!!')


