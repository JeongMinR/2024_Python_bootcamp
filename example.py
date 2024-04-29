import tkinter as tkt

root = tkt.Tk()
root.title("이름")

lbl = tkt.Label(root, text = "이름")
lbl.pack()

txt = tkt.Entry(root)
txt.pack()

btn = tkt.Button(root,text="OK")
btn.pack()

root.mainloop()
