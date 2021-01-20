import tkinter as tk


root = tk.Tk()
root.title('Login')
logEnt = tk.Entry(root, text='aaa')
logEnt.grid(row=0, column=1)
logLab = tk.Label(root, text='Type login:')
logLab.grid(row=0, column=0)
passEnt = tk.Entry(root, show='*')
passEnt.grid(row=1, column=1)
passLab = tk.Label(root, text='Type password:')
passLab.grid(row=1, column=0)
logBut = tk.Button(text='Login')
logBut.grid(row=2, column=0)
exitBut=tk.Button(text='EXIT', command=quit)
exitBut.grid(row=2, column=1)
root.mainloop()