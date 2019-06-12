import tkinter as tk
from tkinter import messagebox

mainwindow=tk.Tk()
mainwindow.title("CALCULATOR")
heading_label=tk.Label(mainwindow,text="First Number")
heading_label.pack()
first_number=tk.Entry(mainwindow)
first_number.pack()
heading_label=tk.Label(mainwindow,text="second number")
heading_label.pack()
second_number=tk.Entry(mainwindow)
second_number.pack()
heading_label=tk.Label(mainwindow,text="Operations")

def takevalueinput():
    first=first_number.get()
    second=second_number.get()
    try:
        first=int(first)
        second=int(second)
        return first,second
    except ValueError:
        if(len(first)==0 or len(second)==0):
            messagebox.showerror("Error","please enter a value")
        else:
            messagebox.showerror("Error","integer value needed")
        quit(0)

def add():
    first,second=takevalueinput()
    result=first+second
    result_label.config(text="operations result is : "+str(result))

def sub():
    first,second=takevalueinput()
    result = first-second
    result_label.config(text="opration result is : "+str(result))
def mul():
    first,second=takevalueinput()
    result = first * second
    result_label.config(text="operation result is : "+str(result))

def div():
    first,second=takevalueinput()
    if(second==0):
        messagebox.showerror("Error","cannot divide the value by 0")
    else:
        result = first / second
        result=round(result,2)
        result_label.config(text="opration result is : " + str(result))
button1=tk.Button(mainwindow,text="+",command=lambda:add())
button1.pack()
button2=tk.Button(mainwindow,text="-",command=lambda:sub())
button2.pack()
button3=tk.Button(mainwindow,text="*",command=lambda:mul())
button3.pack()
button4=tk.Button(mainwindow,text="/",command=lambda:div())
button4.pack()
result_label=tk.Label(mainwindow,text="operations result is : ")
result_label.pack()
mainwindow.mainloop()