import tkinter as tk
import random
from tkinter.constants import END

root = tk.Tk()
root.title("Password Generator v1.0")
root.geometry("350x220")

icon = tk.PhotoImage(file="icon.png") # Создаем переменную и помещаем в нее наше фото
root.iconphoto(False, icon) # Меняем стандартный значек на тот что в переменной
root.resizable(False, False)# Зарет на расширения окна

def gen():
    pwd_ent.delete(0, END)
    stat_ent.delete(0, END)
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = "0123456789"
    d = "!()[]_-?"
    all = a + b + c + d
    try:
        len = len_ent.get()
        len = int(len)
        password = "".join(random.sample(all, len))       # Метод sample генерирует случайную строку
        stat_ent.configure(fg="green",  font=("Arial", 10, "bold"))
        stat_ent.insert(0, "Успешно!")
        pwd_ent.insert(0, password)
    except ValueError:
        stat_ent.configure(fg="red", font=("Arial", 10, "bold"))
        stat_ent.insert(0, "Ошибка!")

len_lbl = tk.Label(root, text="Укажите длину пароля:")
len_lbl.pack()
len_lbl.configure(font=("Courier", 12, "bold"))

len_ent = tk.Entry(root, width=25, borderwidth=3)
len_ent.pack()

pwd_lbl = tk.Label(root, text="Ваш пароль: ")
pwd_lbl.pack()
pwd_lbl.configure(font=("Courier", 12, "bold"))

pwd_ent = tk.Entry(root, width=50, borderwidth=3)
pwd_ent.pack()

stat_lbl = tk.Label(root, text='Статус:')
stat_lbl.pack()
stat_lbl.configure(font=("Courier", 12, "bold"))

stat_ent = tk.Entry(root, width=10, borderwidth=3)
stat_ent.pack()

but_res = tk.Button(root, text="Gen!", width=10, borderwidth=3, fg="red", command=gen)
but_res.pack(pady=10)
but_res.configure(font=("Courier", 14, "bold"))

root.mainloop()