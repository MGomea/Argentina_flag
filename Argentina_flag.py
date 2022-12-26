import turtle as t
import colorsys
t.Screen().bgcolor("skyblue")

t.speed(10)
t.tracer(100)
t.pencolor("white")
t.penup("skyblue")
hue = 0.7
t.hideturtle()

def func():
    global hue
    for i in range(3):
        global hue
        for i in range(3):
            color = colorsys.hsv_to_rgb(hue,1,1)
            hue += 0.001
            t.fillcolor("yellow")
            t.begin_fill()
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(22)
            t.end_fill()
for j in range(400) : 
    func()
    t.goto(8,8)
    t.rt(140)
    
t.bye()
