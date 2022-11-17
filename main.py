import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(50)
colorC = 0.0
t.pensize(3)
for n in range(1000):
    color = colorsys.hsv_to_rgb(colorC, 1, 1)
    colorC += 0.003
    t.pencolor(color)
    for i in range(2):
        t.fd(i)
        t.rt(120)
        t.fd(100)
        t.rt(120)
    t.rt(60 * 2 + 1)
t.done()

