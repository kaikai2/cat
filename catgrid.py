import turtle
from tkinter import PhotoImage

s = turtle.getscreen()

class Object:
    def __init__(self, name, image):
        self.name = name
        self.turtle = turtle.Turtle()
        s.addshape(image)
        self.turtle.shape(image)
        self.turtle.up()

    def checkscreen(self):
        print(self.turtle.xcor())
        print(self.turtle.ycor())
        if self.turtle.xcor() < -400:
            self.turtle.setx(-400)
        if self.turtle.xcor() > 400:
            self.turtle.setx(400)
        if self.turtle.ycor() < -300:
            self.turtle.sety(-300)
        if self.turtle.ycor() > 300:
            self.turtle.sety(300)

    def up(self):
        self.turtle.setheading(90)
        self.turtle.forward(100)
        self.checkscreen()
    
    def down(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.checkscreen()

    def left(self):
        self.turtle.setheading(180)
        self.turtle.forward(100)
        self.checkscreen()

    def right(self):
        self.turtle.setheading(0)
        self.turtle.forward(100)
        self.checkscreen() 



s.setup(1000,800)

mouse = Object("mouse","./mouse.gif")
cat = Object("cat","./cat.gif")



###############

##############
turtle.listen()
turtle.onkey(cat.up,"Up")
turtle.onkey(cat.down,"Down")
turtle.onkey(cat.left,"Left")
turtle.onkey(cat.right,"Right")
turtle.mainloop()



