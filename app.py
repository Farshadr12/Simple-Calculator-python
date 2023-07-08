from tkinter import *

Project = Tk()
Project.title("X Calculator")

display = Entry(Project, width=40, border=5)
display.grid(column=0, row=0, columnspan=3)
output = 0
funStat = 0  # Initialize funStat
# stats = 0:init   1:add   2:sub   3:multi


def keyInput(number):
    display.insert(END, int(number))


def clearDisplay():
    display.delete(0, END)
    global output
    output = 0
    global funStat
    funStat = 0


def additionFun():
    global output
    output += int(display.get())
    global funStat
    funStat = 1
    display.delete(0, END)


def subFun():
    global output
    output = int(display.get())
    global funStat
    funStat = 2
    display.delete(0, END)


def multFun():
    global output
    if output == 0:
        output = int(display.get())
    else:
        output *= int(display.get())
    global funStat
    funStat = 3
    display.delete(0, END)


def equallFun():
    global output
    if funStat == 1:
        output += int(display.get())
    elif funStat == 2:
        output -= int(display.get())
    elif funStat == 3:
        output *= int(display.get())
    display.delete(0, END)
    display.insert(END, output)


key1 = Button(Project, text="1", padx=30, pady=10,
              command=lambda: keyInput(1)).grid(column=0, row=1)
key2 = Button(Project, text="2", padx=30, pady=10,
              command=lambda: keyInput(2)).grid(column=1, row=1)
key3 = Button(Project, text="3", padx=30, pady=10,
              command=lambda: keyInput(3)).grid(column=2, row=1)
key4 = Button(Project, text="4", padx=30, pady=10,
              command=lambda: keyInput(4)).grid(column=0, row=2)
key5 = Button(Project, text="5", padx=30, pady=10,
              command=lambda: keyInput(5)).grid(column=1, row=2)
key6 = Button(Project, text="6", padx=30, pady=10,
              command=lambda: keyInput(6)).grid(column=2, row=2)
key7 = Button(Project, text="7", padx=30, pady=10,
              command=lambda: keyInput(7)).grid(column=0, row=3)
key8 = Button(Project, text="8", padx=30, pady=10,
              command=lambda: keyInput(8)).grid(column=1, row=3)
key9 = Button(Project, text="9", padx=30, pady=10,
              command=lambda: keyInput(9)).grid(column=2, row=3)
key0 = Button(Project, text="0", padx=30, pady=10,
              command=lambda: keyInput(0)).grid(column=0, row=4)

# function buttons
keyeq = Button(Project, text="=", padx=71, pady=10,
               command=equallFun).grid(column=1, row=4, columnspan=2)
keyadd = Button(Project, text="+", padx=15, pady=10,
                command=additionFun).grid(column=3, row=1)
keysub = Button(Project, text="-", padx=16, pady=10,
                command=subFun).grid(column=3, row=2)
keymult = Button(Project, text="*", padx=16, pady=10,
                 command=multFun).grid(column=3, row=3)
keyclr = Button(Project, text="clr", padx=12, pady=3,
                command=clearDisplay).grid(column=3, row=0)

Project.mainloop()
