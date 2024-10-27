#! /usr/bin/env python3
import turtle as t


t.bgcolor("black")
t.speed(-100)
t.hideturtle()

colors = ["red", "yellow", "red", "yellow"]

for i in range(20):
    for c in colors:
        t.color(c)
        t.circle(200 - i, 0)
        t.lt(90)
        t.circle(200 - i, 0)
        t.rt(60)
        t.end_fill()

t.mainloop()
        