from turtle import Turtle
x = int(input("Enter the x position(0-400) : "))
y = int(input("Enter the y position(0-400) : "))
r = float(input("Enter the r value : "))/255
g = float(input("Enter the g value : "))/255
b = float(input("Enter the b value : "))/255
w = int(input("Enter the width of the square : "))
t = Turtle()
t.up()
t.goto(x,y)
t.pencolor(r, g, b)
t.width(w)
t.down()
for i in range(4):
    t.forward(100)
    t.right(90)
