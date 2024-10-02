from turtle import *

def curvemove():

    for i in range(200):
        speed(0)
        right(1)
        forward(1)
def MyOwnImg():
    screensize(800, 800)
    bgcolor('white')
    color('black','green')
    speed(6)
    begin_fill()
    left(140)
    forward(115.65)
    curvemove()
    left(120)
    curvemove()
    forward(115.65)
    end_fill()

for i in range(1,5):
    seth((1-i)*90)
    MyOwnImg()
seth(-60)
color('brown')
pensize(10)
for i in range(1,500):
    right(0.25)
    forward(1)

done()

