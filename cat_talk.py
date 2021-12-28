import turtle

s = turtle.getscreen()
image = "~/cat.gif"

s.addshape(image)
cat = turtle.Turtle()
cat.shape(image)

cat.up()
cat.setheading(90);
cat.forward(100);
turtle.up()
turtle.hideturtle()

def cattalk(word):
    turtle.setheading(270)
    turtle.forward(50)
    turtle.write(word+"\n",align="left", font=("Arial", 18, "normal"))


###############

cattalk("I'm a string uppercase cat!")

a=[1,2,3,4,5]

for n in a:
    cattalk(str(n))


########
turtle.mainloop()




