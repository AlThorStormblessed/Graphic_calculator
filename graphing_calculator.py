from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import random

global pi_
global e_
pi_ = pi
e_ = e
expression = ""
expracius = ""


def cot(num):
    x = tan(num)
    return x ** (-1)


def cosec(num):
    x = sin(num)
    return x ** (-1)


def sec(num):
    x = cos(num)
    return x ** (-1)


global deg
deg = radians

global rad
rad = degrees


def roun():
    global ans
    ans = float(ans)
    if ans // 1 + 0.5 >= ans:
        ans = ans // 1
    elif ans // 1 + 0.5 < ans:
        ans = ans // 1 + 1
    equation.set(str(ans))


def leave():
    exit()


def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)


def addpress(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)


func = 0


def equalpress():
    global expression
    global expracius
    global func

    if not func:
        expracius = expression
        equation.set(
            "Enter range for the graph (lower limit and upper limit with space)"
        )
        func = 1

    elif func:
        func = 0
        num = expression.split()

        lower = float(num[0])
        upper = float(num[1])

        ##list_1 = [eval(str(expracius)) for x in np.arange(lower, upper+1, 0.001)]
        list_1 = []
        not_list = []
        for x in np.arange(lower, upper, 0.01):
            try:
                list_1.append(eval(str(expracius)))
            except:
                not_list.append(x)

        b = [i for i in np.arange(lower, upper, 0.01) if i not in not_list]

        plt.plot(
            b, list_1, color=random.choice(("blue", "red", "black", "green", "orange"))
        )

        plt.legend(["y = " + expracius])
        plt.title("Awesome graphs!!!")
        plt.xlabel("x")
        plt.ylabel(f"f({expracius})")
        plt.grid(linestyle="-")
        plt.show()

        expracius = ""
        expression = ""
        equation.set("")
        list_1, b = [], []

    expression = ""


def clr():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set(expression)


if __name__ == "__main__":
    root = Tk()
    root.configure(background="black")
    root.title("Graphing Calculator")
    print(root)
    root.geometry("418x295")

    root.bind("1", lambda a: press("1"))
    root.bind("2", lambda a: press("2"))
    root.bind("3", lambda a: press("3"))
    root.bind("4", lambda a: press("4"))
    root.bind("5", lambda a: press("5"))
    root.bind("6", lambda a: press("6"))
    root.bind("7", lambda a: press("7"))
    root.bind("8", lambda a: press("8"))
    root.bind("9", lambda a: press("9"))
    root.bind("0", lambda a: press("0"))
    root.bind(".", lambda a: press("."))
    root.bind("x", lambda a: press("x"))
    root.bind("<space>", lambda a: press(" "))
    root.bind("<BackSpace>", lambda a: clr())
    root.bind("(", lambda a: press("("))
    root.bind(")", lambda a: press(")"))

    root.bind("+", lambda a: addpress("+"))
    root.bind("-", lambda a: addpress("-"))
    root.bind("/", lambda a: addpress("/"))
    root.bind("*", lambda a: addpress("*"))
    root.bind("^", lambda a: addpress("**"))
    root.bind("=", lambda a: equalpress())

    root.bind("c", lambda a: clear())
    root.bind("q", lambda a: leave())

    equation = StringVar()
    texta = StringVar()

    expression_field = Entry(root, text=equation)
    expression_field.grid(
        row=0,
        column=0,
        rowspan=2,
        columnspan=8,
        ipadx=150,
        ipady=15,
        sticky=NW + NE + SW + SE,
    )

    equation.set("Enter your expression")

    excla = Button(
        root,
        text="factorial x",
        command=lambda: press("factorial("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    excla.grid(row=2, column=0, sticky=NW + NE + SW + SE)

    log_ = Button(
        root,
        text="log10",
        command=lambda: press("log10("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    log_.grid(row=4, column=0, sticky=NW + NE + SW + SE)

    ln_ = Button(
        root,
        text="ln",
        command=lambda: press("log("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    ln_.grid(row=5, column=0, sticky=NW + NE + SW + SE)

    sqrt_ = Button(
        root,
        text="√x",
        command=lambda: press("sqrt("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    sqrt_.grid(row=3, column=0, sticky=NW + NE + SW + SE)

    cot_ = Button(
        root,
        text="cot x",
        command=lambda: press("cot("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    cot_.grid(row=7, column=1, sticky=NW + NE + SW + SE)

    sin_ = Button(
        root,
        text="sin x",
        command=lambda: press("sin("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    sin_.grid(row=2, column=1, sticky=NW + NE + SW + SE)

    deg_ = Button(
        root,
        text="Enter Degrees",
        command=lambda: press("deg("),
        height=2,
        width=16,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    deg_.grid(row=7, column=1, sticky=NW + NE + SW + SE, columnspan=2)

    rad_ = Button(
        root,
        text="Enter Radians",
        command=lambda: press("rad("),
        height=2,
        width=16,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    rad_.grid(row=7, column=3, sticky=NW + NE + SW + SE, columnspan=2)

    cos_ = Button(
        root,
        text="cos x",
        command=lambda: press("cos("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    cos_.grid(row=3, column=1, sticky=NW + NE + SW + SE)

    tan_ = Button(
        root,
        text="tan x",
        command=lambda: press("tan("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    tan_.grid(row=4, column=1, sticky=NW + NE + SW + SE)

    sec_ = Button(
        root,
        text="sec x",
        command=lambda: press("sec("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    sec_.grid(row=5, column=1, sticky=NW + NE + SW + SE)

    cosec_ = Button(
        root,
        text="cosec x",
        command=lambda: press("cosec("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    cosec_.grid(row=6, column=1, sticky=NW + NE + SW + SE)

    cot_ = Button(
        root,
        text="cot x",
        command=lambda: press("cot("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    cot_.grid(row=6, column=0, sticky=NW + NE + SW + SE)

    button1 = Button(
        root,
        text="1",
        command=lambda: press(1),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button1.grid(row=2, column=2, sticky=NW + NE + SW + SE)

    button2 = Button(
        root,
        text="2",
        command=lambda: press(2),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button2.grid(row=2, column=3, sticky=NW + NE + SW + SE)

    button3 = Button(
        root,
        text="3",
        command=lambda: press(3),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button3.grid(row=2, column=4, sticky=NW + NE + SW + SE)

    button4 = Button(
        root,
        text="4",
        command=lambda: press(4),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button4.grid(row=3, column=2, sticky=NW + NE + SW + SE)

    button5 = Button(
        root,
        text="5",
        command=lambda: press(5),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button5.grid(row=3, column=3, sticky=NW + NE + SW + SE)

    button6 = Button(
        root,
        text="6",
        command=lambda: press(6),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button6.grid(row=3, column=4, sticky=NW + NE + SW + SE)

    button7 = Button(
        root,
        text="7",
        command=lambda: press(7),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button7.grid(row=4, column=2, sticky=NW + NE + SW + SE)

    button8 = Button(
        root,
        text="8",
        command=lambda: press(8),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button8.grid(row=4, column=3, sticky=NW + NE + SW + SE)

    button9 = Button(
        root,
        text="9",
        command=lambda: press(9),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button9.grid(row=4, column=4, sticky=NW + NE + SW + SE)

    button0 = Button(
        root,
        text="0",
        command=lambda: press(0),
        height=2,
        width=7,
        fg="red",
        bg="snow",
        activeforeground="blue",
        activebackground="red",
    )
    button0.grid(row=5, column=2, sticky=NW + NE + SW + SE)

    equal = Button(
        root,
        text="=",
        command=lambda: equalpress(),
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    equal.grid(row=5, column=3, sticky=NW + NE + SW + SE)

    clear_ = Button(
        root,
        text="Clear('c')",
        command=lambda: clear(),
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    clear_.grid(row=5, column=4, sticky=NW + NE + SW + SE)

    deci = Button(
        root,
        text=".",
        command=lambda: press("."),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    deci.grid(row=6, column=2, sticky=NW + NE + SW + SE)

    add = Button(
        root,
        text="+",
        command=lambda: addpress("+"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    add.grid(row=2, column=5, sticky=NW + NE + SW + SE)

    sub = Button(
        root,
        text="-",
        command=lambda: addpress("-"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    sub.grid(row=3, column=5, sticky=NW + NE + SW + SE)

    mult = Button(
        root,
        text="x",
        command=lambda: addpress("*"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    mult.grid(row=4, column=5, sticky=NW + NE + SW + SE)

    div = Button(
        root,
        text="/",
        command=lambda: addpress("/"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    div.grid(row=5, column=5, sticky=NW + NE + SW + SE)

    mod = Button(
        root,
        text="%",
        command=lambda: addpress("%"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    mod.grid(row=6, column=6, sticky=NW + NE + SW + SE)

    rounder = Button(
        root,
        text="Space",
        command=lambda: press(" "),
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    rounder.grid(row=7, column=0, sticky=NW + NE + SW + SE)

    answer = Button(
        root,
        text="X",
        command=lambda: press("x"),
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    answer.grid(row=6, column=3, sticky=NW + NE + SW + SE)

    expo = Button(
        root,
        text="x^y",
        command=lambda: addpress("**"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    expo.grid(row=6, column=5, sticky=NW + NE + SW + SE)

    leaver = Button(
        root,
        text="Quit",
        command=lambda: leave(),
        height=2,
        width=16,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    leaver.grid(row=7, column=5, sticky=NW + NE + SW + SE, columnspan=2)

    pi = Button(
        root,
        text="π",
        command=lambda: press(pi_),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    pi.grid(row=4, column=6, sticky=NW + NE + SW + SE)

    e = Button(
        root,
        text="e",
        command=lambda: press(e_),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    e.grid(row=5, column=6, sticky=NW + NE + SW + SE)

    brack1 = Button(
        root,
        text="(",
        command=lambda: press("("),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    brack1.grid(row=2, column=6, sticky=NW + NE + SW + SE)

    brack2 = Button(
        root,
        text=")",
        command=lambda: press(")"),
        height=2,
        width=7,
        fg="dark blue",
        bg="powder blue",
        activeforeground="blue",
        activebackground="red",
    )
    brack2.grid(row=3, column=6, sticky=NW + NE + SW + SE)

    clearo_ = Button(
        root,
        text="CE",
        command=lambda: clr(),
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    clearo_.grid(row=6, column=4, sticky=NW + NE + SW + SE)

    for i in range(0, 7):
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)

    root.grid_rowconfigure(7, weight=1)

    root.update_idletasks()
    root.update()
