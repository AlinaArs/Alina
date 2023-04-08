from tkinter import *

def click():
    window2 = Tk()
    window2.title('Hi')
    lbl = Label(window2, text=f'Привет, {ent.get()}, тебе {ent2.get()} лет')
    lbl.grid(column=0, row=0)
    window2.mainloop()



window = Tk()
window.title('Hi')
lbl = Label(window, text = 'ФИО')
lbl.grid(column = 0, row = 0)
lbl2 = Label(window, text = 'Возраст')
lbl2.grid(column = 1, row = 2)

window.geometry('400x200')
ent = Entry(window, width = 10)
ent2 = Entry(window, width = 10)
ent.grid (column = 1, row = 0)
ent2.grid (column = 2, row =2)
btn = Button(window, text = 'accept', command = click)
btn.grid(column = 3, row = 3)

window.mainloop()