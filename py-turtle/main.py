import turtle
from math import sqrt

t = turtle.Turtle()

turtle.Screen().bgcolor("#111111")

t.pensize(2)
t.pencolor("white")
t.speed(0)
t.up()


def triangle(a, n):
	for i in range(n):
		t.pencolor(1 - (i / 33.3), i / 100, i / 10)
		t.backward(a / 2)
		t.right(90)
		t.forward(a / (2 * sqrt(3)))
		t.left(90)
		t.down()
		t.forward(a)
		t.left(120)
		t.forward(a)
		t.left(120)
		t.forward(a)
		t.left(120)
		t.up()
		t.home()
		a *= 1.25


triangle(50, 10)

t.hideturtle()
turtle.done()
