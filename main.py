from tkinter import *
from tkinter import messagebox, Menu, scrolledtext, filedialog


def click():
    file = filedialog.askopenfilename()
    f = open(file)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def click2():
    file_name = filedialog.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()


def click3():
    window2 = Tk()
    window2.title('Новое окно')
    window2.geometry('600x400')

    txt2 = scrolledtext.ScrolledText(window2, width=40, height=20)
    txt2.grid(column=0, row=4)


window = Tk()
window.title('Блокнот')
text = Text(width=50, height=25)
text.grid(columnspan=2)

window.geometry('600x400')

menu = Menu(window)
new_item = Menu(menu, tearoff= 0)
new_item.add_command(label='Открыть', command= click)
new_item.add_command(label='Сохранить как', command=click2)
new_item.add_command(label='Новый файл', command=click3)
menu.add_cascade(label='Меню', menu=new_item)

window.configure(menu=menu)



txt = scrolledtext.ScrolledText(window, width=40, height=20)
txt.grid(column=0, row=4)



window.mainloop()