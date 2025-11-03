# Python Turtle Artist
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightblue")
OTHER_OBJECT = {
    "lightyellow": "#F5DD90",
    "nightblue": "#324376",
    "brown": "#A27E6F",
    "dark green": "#004400",
    "mentis": "#79B473",
    "cambridgeblue": "#70A37F",
    "midnight green": "#07393C",
}
wn.bgcolor(OTHER_OBJECT["nightblue"])
t = turtle.Turtle()


def star(length: int):
    t.color(OTHER_OBJECT["lightyellow"])
    # t.color("yellow")
    t.backward(length / 2)
    for _ in range(5):
        t.forward(length)
        t.right(144)


def cone(radius: int, color: str, fillcolor: str):
    t.color(color)
    t.fillcolor(fillcolor)
    if radius > 0:
        t.width(3)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.left(90)
        t.penup()
        t.forward(radius * 0.1 + 5)
        t.pendown()
        t.right(90)
        cone(radius - 2, color, fillcolor)


t.speed(0.1)
t.penup()
t.goto(-700, -300)
t.begin_fill()
for _ in range(2):
    t.color(OTHER_OBJECT["brown"])
    t.forward(2000)
    t.right(90)
    t.forward(500)
    t.right(90)
t.end_fill()
for _ in range(200):
    t.penup()
    t.goto(random.randint(-600, 600), random.randint(-250, 500))
    t.pendown()
    star(10)
    t.penup()
t.goto(0, -400)
t.pendown()
cone(100, "green", OTHER_OBJECT["dark green"])
t.begin_fill()
star(50)
t.end_fill()
t.penup()
t.goto(-250, -500)
t.pendown()
cone(80, OTHER_OBJECT["mentis"], OTHER_OBJECT["midnight green"])
t.begin_fill()
star(50)
t.end_fill()
t.penup()
t.goto(250, -500)
t.pendown()
cone(80, OTHER_OBJECT["cambridgeblue"], OTHER_OBJECT["midnight green"])
t.begin_fill()
star(50)
t.end_fill()
wn.exitonclick()
