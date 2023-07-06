import turtle
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'
t = turtle.Turtle()

def galka():
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

for i in range(2):
    galka()
turtle.done()