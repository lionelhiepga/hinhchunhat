import turtle

t = turtle.Turtle()

m = 150
n = 50

for i in range(0,2):
    t.forward(n)
    t.left(90)
    t.forward(m)
    t.left(90)
    
turtle.end_fill()
