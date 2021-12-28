import turtle

s = turtle.getscreen()
image = "~/cat.gif"

s.addshape(image)
cat = turtle.Turtle()
cat.shape(image)

mouse = turtle.Turtle()
mouse_image = "~/mouse.gif"
s.addshape(mouse_image)
mouse.shape(mouse_image)
mouse.up()
mouse.setx(300)
mouse.sety(200)

def check_mouse():
    
    if int(cat.xcor()) == int(mouse.xcor()) and int(cat.ycor()) == int(mouse.ycor()):
        mouse.setheading(270)
        mouse.forward(100)
    
    #return true if mouse is catched

def up():
    cat.setheading(90)
    cat.forward(100)
    check_mouse()
   
def down():
    cat.setheading(270)
    cat.forward(100)
    check_mouse()

def left():
    cat.setheading(180)
    cat.forward(100)
    check_mouse()

def right():
    cat.setheading(0)
    cat.forward(100)
    check_mouse()
###############
cat.up()


##############
turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.mainloop()




