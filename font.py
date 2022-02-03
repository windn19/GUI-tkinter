import tkinter as tk


def dd(arg=None):
    print(arg)
    d = int(field.get())
    month = ["зима", "весна", "лето", "осень"]
    if d // 3 == 0 or d // 3 == 4:
        k = 0
    else:
        k = d // 3
    lbl['text'] = month[k]


window = tk.Tk()
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2], minsize=40)
window.title('Дни недели - 1')
field = tk.Entry(master=window, width=3)
field.bind('<Return>', dd)
btn = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=dd)
lbl = tk.Label(master=window, text='NN')
lbl.grid(row=0, column=2, sticky='nsew')
btn.grid(row=0, column=1, sticky='nsew')
field.grid(row=0, column=0, sticky='nsew')
window.geometry('210x40+700+400')

window.mainloop()
