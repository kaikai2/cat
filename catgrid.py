import turtle
from random import randint

from PIL import Image

catImages = Image.open("./cat.gif")

print(dir(catImages))
print(catImages.n_frames)
print(catImages.getdata())
catImages.seek(1)
print(catImages.getdata())

def getactualx(x):
    return leftbottom_x + x*100 + 100

def getactualy(y):   
    return leftbottom_y + y*100 + 100


s = turtle.getscreen()
s.setup(1000,800)
leftbottom_y = - s.window_height()/2
leftbottom_x = - s.window_width()/2
max_y = int(s.window_height() / 100 -2)
max_x = int(s.window_width() / 100 - 2)

turtle.hideturtle()
turtle.speed(0)
for ix in range (max_x+1):
    turtle.penup()
    turtle.goto([getactualx(ix), getactualy(0)])
    turtle.pendown()
    turtle.goto([getactualx(ix), getactualy(max_y)])

for iy in range (max_y+1):
    turtle.penup()
    turtle.goto([getactualx(0), getactualy(iy)])
    turtle.pendown()
    turtle.goto([getactualx(max_x), getactualy(iy)])

class Object:
    def __init__(self, name, image):
        self.name = name
        self.turtle = turtle.Turtle()
        s.addshape(image)
        self.turtle.shape(image)
        self.turtle.up()
        self.x=0
        self.y=0
        self.update()
        

    def update(self):
        self.turtle.setx(getactualx(self.x))
        self.turtle.sety(getactualy(self.y))
        print(self.turtle.xcor())
        print(self.turtle.ycor())

    def getx(self):
        return self.x
    
    def setx(self, x):
        self.x = x

    def gety(self):
        return self.y

    def sety(self, y):
        self.y = y

    def up(self):
        if (self.y < max_y):
            self.y = self.y + 1
        self.update()

    def down(self):
        if self.y >= 1 :
            self.y = self.y - 1
        self.update()

    def left(self):
        if self.x >= 1:
            self.x = self.x - 1
        self.update()

    def right(self):
        if self.x < max_x:
            self.x = self.x +1 
        self.update()





mouse = Object("mouse","./mouse.gif")
cat = Object("cat","./cat.gif")
mouse.setx(randint(0,max_x))
mouse.sety(randint(0,max_y))
mouse.update()

###############

##############
turtle.listen()
turtle.onkey(cat.up,"Up")
turtle.onkey(cat.down,"Down")
turtle.onkey(cat.left,"Left")
turtle.onkey(cat.right,"Right")

turtle.onkey(mouse.up,"w")
turtle.onkey(mouse.down,"s")
turtle.onkey(mouse.left,"a")
turtle.onkey(mouse.right,"d")
print ("xscale")

turtle.mainloop()



