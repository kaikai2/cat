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
    if cat.xcor() < -400:
        cat.setx(-400)
    if cat.xcor() > 400:
        cat.setx(400)
    if cat.ycor() < -300:
        cat.sety(-300)
    if cat.ycor() > 300:
        cat.sety(300)


def up():
    cat.setheading(90)
    cat.forward(100)
    checkscreen()
    

def down():
    cat.setheading(270)
    cat.forward(100)
    checkscreen()

def left():
    cat.setheading(180)
    cat.forward(100)
    checkscreen()
def right():
    cat.setheading(0)
    cat.forward(100)
    checkscreen()
###############
for i  in range(3):
    up()       
while (True):
    for i in range(4):
        right()
    for i in range(6):
        down()
    for i in range(8):
        left()
    for i in range(6):
        up()
    for i in range(4):
        right()
##############
turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.mainloop()



