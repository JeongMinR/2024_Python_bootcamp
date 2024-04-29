import tkinter as tkt

def on_click(number):
    entry.insert(tkt.END, number)

root = tkt.Tk()
root.title("계산기")

photo = tkt.PhotoImage(file="C:/Users/USER/Desktop/haedal/bootcamp/icon.png")
root.iconphoto(False, photo)
entry = tkt.Entry(root, width=20, borderwidth=12, fon=("Verdana", 13), justify="right") 
entry.grid(row=0, column=0, columnspan=4, pady=10)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command, bg=bg, borderwidth=3)
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')

for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n),bg='gainsboro') 
create_button("0", 5, 0, lambda: on_click(0), columnspan=2,bg='gainsboro') 

def on_clear():
    entry.delete(0, tkt.END)
create_button("C", 1, 0, on_clear, bg='gray70')   

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = int(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = int(entry.get())
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        entry.insert(0, first_num + second_num)
    elif 연산자 == "-":
        entry.insert(0, first_num - second_num)
    elif 연산자 == "*":
        entry.insert(0, first_num * second_num)
    elif 연산자 == "/":
        entry.insert(0, first_num / second_num)

create_button("%", 1, 2, None, bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')       

root. mainloop()