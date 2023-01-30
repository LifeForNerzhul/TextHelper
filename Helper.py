import tkinter as tk
import pyperclip

def up():
    text_input.delete(1.0, 'end')
    text_input.insert('1.0', text_output.get(1.0, 'end'))

def copy():
    pyperclip.copy(text_output.get(1.0, 'end'))

def clearAll():
    text_output.delete(1.0, 'end')
    text_input.delete(1.0, 'end')
    text_find.delete(0, 'end')
    text_change.delete(0, 'end')

def get_data():
    _input=(text_input.get('1.0',"end-1c"))
    _find=text_find.get()
    _change=text_change.get()
    data=_input.replace(_find,_change)
    text_output.delete(1.0, 'end')
    text_output.insert(1.0, data)


win = tk.Tk()
win.title('Helper')
win.geometry("900x1000")
win.config(bg='#323232')
win.resizable(width=False, height=False)  # не изменяемый размер окна

# Кнопки
btn1=tk.Button(win, text='Выполнить',
               command= get_data,
               font='Arial',
               bg='#696969',
               fg='#FFFAFA',
               activebackground='#808080'
               )
btn2=tk.Button(win, text='Копировать вывод',
               command= copy,
               font='Arial',
               bg='#696969',
               fg='#FFFAFA',
               activebackground='#808080'
               )
btn3=tk.Button(win, text='Очистить всё',
               command= clearAll,
               font='Arial',
               bg='#696969',
               fg='#FFFAFA',
               activebackground='#808080'
               )
btn4=tk.Button(win, text='↑',
               command= up,
               font='Arial',
               bg='#696969',
               fg='#FFFAFA',
               activebackground='#808080',
               width=2,
               height=2
               )
# Надписи
label_find= tk.Label(win, font='Arial', text= 'Найти:', bg='#323232',fg='#FFFFFF')
label_change= tk.Label(win, font='Arial', text= 'Заменить на:', bg='#323232',fg='#FFFFFF')
label_input= tk.Label(win, font='Arial', text= 'Ввод:', bg='#323232',fg='#FFFFFF')
label_output= tk.Label(win, font='Arial', text= 'Вывод:', bg='#323232',fg='#FFFFFF')

# Окна ввода
text_input = tk.Text(win,height=25,width=50)
text_find = tk.Entry(win)
text_change = tk.Entry(win)

# Окна вывода
text_output = tk.Text(win,height=25,width=50)

btn1.place(relx= .75, rely= .50, anchor= 'center')
btn2.place(relx= .75, rely= .75, anchor= 'center')
btn3.place(relx= .75, rely= .90, anchor= 'center')
btn4.place(relx= .45, rely= .50, anchor= 'center')


text_input.place(relx= .25, rely= .25, anchor= 'center')
text_find.place(relx= .75, rely= .18, anchor= 'center')
text_change.place(relx= .75, rely= .28, anchor= 'center')

label_find.place(relx= .75, rely= .15, anchor= 'center')
label_change.place(relx= .75, rely= .25, anchor= 'center')
label_input.place(relx= .25, rely= .03, anchor= 'center')
label_output.place(relx= .25, rely= .53, anchor= 'center')

text_output.place(relx= .25, rely= .75, anchor= 'center')

# Обработка горячих клавиш
win.event_add('<<Paste>>', '<Control-igrave>')
win.event_add("<<Copy>>", "<Control-ntilde>")

win.mainloop()