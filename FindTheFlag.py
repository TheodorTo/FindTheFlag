import turtle
import random
from tkinter import *
from tkinter import messagebox
window = Tk()

turtle1 = turtle.Turtle()

run = True
points = 0
lives = 3
displaypoints=""

a = True


def germany():
    turtle1.fillcolor('black')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(100, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.color('red')
    turtle1.goto(100, -30)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.color('yellow')
    turtle1.goto(100, -60)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.hideturtle()


def italy():
    turtle1.pencolor('green')
    turtle1.fillcolor('green')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(100, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.pencolor('white')
    turtle1.fillcolor('white')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(150, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.pencolor('red')
    turtle1.fillcolor('red')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(200, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()


def russia():
    turtle1.pencolor('white')

    turtle1.fillcolor('white')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(100, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.color('blue')
    turtle1.goto(100, -30)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.color('red')
    turtle1.goto(100, -60)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(150)
        turtle1.rt(90)
        turtle1.fd(30)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.hideturtle()


def france():
    turtle1.pencolor('blue')
    turtle1.fillcolor('blue')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(100, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.pencolor('white')
    turtle1.fillcolor('white')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(150, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.pencolor('red')
    turtle1.fillcolor('red')
    turtle1.pensize(5)
    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(200, 0)
    turtle1.pendown()
    turtle1.begin_fill()
    for i in range(2):
        turtle1.fd(50)
        turtle1.rt(90)
        turtle1.fd(90)
        turtle1.rt(90)
    turtle1.end_fill()
    turtle1.penup()


def clicked():
    global points
    global run
    global a
    global displaypoints
    turtle1.reset()
    turtle1.speed(200)
    flag = random.choice(flags)
    flag()
    a = False

    while a is False:
        answer = txt.get()


        if answer == flag.__name__:
            points = points + 1
            displaypoints=points

            res = messagebox.showinfo("Info Popup", displaypoints)
            print(res)
            print("yea")

            if points == 4:
                run = False

        else:
            print("")
        a = True






flags = [germany, italy, france, russia]

btn1 = Button(window, text="done", command=clicked)
btn1.grid(column=1, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=0)

turtle1.reset()
turtle1.speed(200)
flag = random.choice(flags)
flag()
a = False

while a is False:
    answer = txt.get()


    if answer == flag.__name__:
        points = points + 1
        displaypoints=points


        print(res)
        print("yea")
        flags.remove(flag)

        if points == 4:
            run = False

    else:
        print("")
    a = True





res = messagebox.showinfo("Info Popup", displaypoints)

turtle.done()
window.mainloop()
