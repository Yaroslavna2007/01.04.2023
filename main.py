from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton

window = Tk() #создание окна
window.title('Homework') #название окна
window.geometry('400x400') #размеры окна

txt = Label(window,text = 'Hi', font = ('Arial Bold', 30)) #текст в окне
txt.grid(column = 0, row = 0 ) #размещение текста в окне

def Click():
    r = t.get()
    txt.configure(text = 'Hello ' + r)

kn = Button(window, text = 'Ok',bg = 'black',fg = 'white',command= Click) #создание кпопки
kn.grid(column = 1, row = 0 ) #размещение кнопки в окне

t = Entry(window, width= 20) #текстовая строка
t.grid(column = 0,row = 1) #размещение текстовой строки в окне
t.focus() # поле сразу активно для ввода

e = Combobox(window)
e.grid(column=3,row=1)
e['values'] = ('не выбрано',1,2,3)
e.current(0)

chk_state = BooleanVar()
chk_state.set(False)
p = Checkbutton(window, text = 'выбрать', var = chk_state)
p.grid(column=0,row=2)



window.mainloop() #окно не исчезает с экрана до его закрытия




