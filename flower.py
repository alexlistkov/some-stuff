import turtle, Tkinter

def draw_all():
    window = turtle.Screen()
    window.bgcolor('blue')
    # create class rhombus
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed('max')
    for i in range(0,36):
        draw_rhombus(brad)
        brad.right(10)
    draw_line()

    window.exitonclick()


def draw_rhombus(some_rhombus):
    for i in range (1,3):
        some_rhombus.forward(100)
        some_rhombus.right(45)
        some_rhombus.forward(100)
        some_rhombus.right(135)

def draw_line():
	leo = turtle.Turtle()
	leo.color('lightgreen')
	leo.speed('max')
	leo.forward(0)
	leo.right(90)
	leo.forward(250)


draw_all()
