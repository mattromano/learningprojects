from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*.6
    t1.insert(END, miles)

def kg_conversion():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)
    pounds = float(e1_value.get())*2.20462
    t2.insert(END,pounds)
    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)


b1 = Button(window, text='Execute',command=kg_conversion)
b1.grid(row=0,column=3)

label = Label(window, text='Kg')
label.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=3)

window.mainloop()
()