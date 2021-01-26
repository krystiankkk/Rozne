import tkinter as tk
from functools import partial
import psycopg2

def adminpanel():
    root=tk.Tk()
    root.mainloop()
def validate(login, password):
    login = logent.get()
    password = passent.get()
    at=+1
    try:
        conn = psycopg2.connect(user=login, password=password, dbname='postgres', host='localhost')
        val = True
        root.destroy()
        adminpanel()
    except:
        print('inicorret',at)
        val = False
    return val

root = tk.Tk()
root.title('Login')
loginlab = tk.Label(root, text='Login:')
loginlab.grid(column=0, row=0)
passlab = tk.Label(root, text='Password:')
passlab.grid(column=0, row=1)
login = ''
logent = tk.Entry(root, show='*', textvariable=login)
logent.grid(column=1, row=0)
password=''
passent = tk.Entry(root, show='*', textvariable=password)
passent.grid(column=1, row=1)
validate = partial(validate, login, password)
loginbut=tk.Button(text='Login', command=(validate))
loginbut.grid(column=0, row=2)
exitbut=tk.Button(root, text='EXIT', command=quit)
exitbut.grid(column=1, row=2)
root.mainloop()