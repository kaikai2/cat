import turtle
from tkinter import PhotoImage

s = turtle.getscreen()


cat = turtle.Turtle()
cat_image = "./cat.gif"
s.addshape(cat_image)
cat.shape(cat_image)
cat.up()

mouse = turtle.Turtle()
smaller = PhotoImage(file="./mouse.gif").zoom(1, 1)

mouse_image = "./mouse.gif"
s.addshape(mouse_image, turtle.Shape("image", smaller))
mouse.shape(mouse_image)
mouse.up()


def checkscreen():
    print(cat.xcor())
    print(cat.ycor())
    if cat.xcor() < 0:
        cat.setx(3)
    if cat.xcor() > s.window_width():
        cat.setx(s.window_width())
    if cat.ycor() < 0:
        cat.sety(3)
    if cat.ycor() > s.window_height():
        cat.sety(s.window_height())


def up():
    cat.setheading(90)
    cat.forward(100)
    checkscreen()
    

def down():
    cat.setheading(270)
    cat.forward(100)
    checkscreen()
def left():
    cat.setheading(0)
    cat.forward(100)
    checkscreen()
def right():
    cat.setheading(180)
    cat.forward(100)
    checkscreen()
###############



##############
turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.mainloop()



