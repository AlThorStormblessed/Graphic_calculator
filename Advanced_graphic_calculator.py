from tkinter import *
from math import pi
from math import e
from math import *
import tkinter.font as tkFont

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
    global expracius
    expression = expression + str(num)

    expracius += expression
    expression = ""

    equation.set(expression)


def equalpress():
    try:
        global expression
        global ans
        global expracius

        expracius += expression
        ans = ""

        total = str(eval(expracius))

        equation.set(total)

        ans = total

        expression = ""
        expracius = ans

    except:
        equation.set("Error. Clear and try again.")
        expression = ""


def clr():
    global expression
    global expracius
    expression = expression[:-1]
    equation.set(expression)


def clear():
    global expression
    global expracius
    expression = ""
    expracius = ""
    equation.set("Cleared")


def font_change(event):
    if event.widget != root:
        return None

    # Base size
    normal_width = 400
    normal_height = 300

    root.update()

    # Get screen size
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    # Get percentage of screen size from Base size
    percentage_width = screen_width / (normal_width / 100)
    percentage_height = screen_height / (normal_height / 100)

    # Make a scaling factor, this is bases on average percentage from
    # width and height.
    scale_factor = ((percentage_width + percentage_height) / 2) / 100

    # Set the fontsize based on scale_factor,
    # if the fontsize is less than minimum_size
    # it is set to the minimum size

    minimum_size = 8
    if scale_factor > minimum_size / 11:
        font_size = int(11 * scale_factor)

    else:
        font_size = minimum_size

    fontsize.configure(size=font_size)


if __name__ == "__main__":
    root = Tk()
    root.configure(background="black")
    root.title("Calculator")
    root.geometry("400x300")
    fontsize = tkFont.Font(size=11)

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

    root.bind("+", lambda a: addpress("+"))
    root.bind("-", lambda a: addpress("-"))
    root.bind("/", lambda a: addpress("/"))
    root.bind("*", lambda a: addpress("*"))
    root.bind("^", lambda a: addpress("**"))
    root.bind("=", lambda a: equalpress())

    root.bind("c", lambda a: clear())
    root.bind("q", lambda a: leave())
    root.bind("<BackSpace>", lambda a: clr())
    root.bind("<Configure>", font_change)

    equation = StringVar()
    texta = StringVar()

    expression_field = Entry(root, text=equation, font=fontsize)
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
        text="x!",
        command=lambda: press("factorial("),
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        text="C",
        command=lambda: clear(),
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        text="Round",
        command=lambda: roun(),
        font=fontsize,
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
        text="Answer",
        command=lambda: press(ans),
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
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
        font=fontsize,
        height=2,
        width=7,
        fg="dark blue",
        bg="light goldenrod",
        activeforeground="blue",
        activebackground="red",
    )
    clearo_.grid(row=6, column=4, sticky=NW + NE + SW + SE)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    for i in range(1, 7):
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)

    root.grid_rowconfigure(7, weight=1)

    root.update_idletasks()
    root.update()
