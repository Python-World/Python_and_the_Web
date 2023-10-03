import time
import turtle

wn = turtle.Screen()
spongebob = turtle.Turtle()  # create a new turtle named spongebob
colors = ["red", "blue", "green"]
spongebob.speed(0)
spongebob.shape("turtle")
spongebob.penup()
spongebob.hideturtle()
spongebob.left(60)

for i in range(1, 13):
    spongebob.color(colors[i % 3])
    spongebob.pensize(2)
    spongebob.forward(140)
    spongebob.pendown()
    spongebob.forward(30)
    spongebob.penup()
    spongebob.forward(30)
    spongebob.write(i, font=("Arial", 12, "normal"), align="center")
    spongebob.backward(200)
    spongebob.pensize(1)
    for j in range(4):
        spongebob.right(6)
        spongebob.forward(140)
        spongebob.pendown()
        spongebob.forward(20)
        spongebob.penup()
        spongebob.backward(160)
    spongebob.right(6)

spongebob.color("orange")
spongebob.shape("circle")
spongebob.stamp()
spongebob.pendown()
# It's spongebob's rest time so...
# our new turtles a,b,c will now draw Hour, Minute and Second hand respectively for us untill he dies...!!! (big evil laugh)
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
a.speed(0)
b.speed(0)
c.speed(0)
a.hideturtle()
b.hideturtle()
c.hideturtle()
a.pensize(5)
b.pensize(2)
c.pensize(1)

starttime = time.time()

while True:
    t = time.localtime()
    h = t.tm_hour  # we will work on 12 hour time instead of 24 hour time
    m = t.tm_min
    s = t.tm_sec

    print(f"{h:02}:{m:02}:{s:02} {'am' if h < 12 else 'pm'}")

    # draw Hour Hand
    angle = (
        h * 30 + m * (1 / 2) + s * (1 / 120) - 90
    )  # subtract 90 deg bcz turtle starts at 3 o'clock not at 12 o'clock
    a.clear()  # clear previous drawings drawn by our turtle
    a.right(angle)
    a.forward(100)
    a.backward(100)
    a.left(angle)

    # draw Minute Hand
    angle = m * 6 + s * (1 / 10) - 90
    b.clear()  # clear previous drawings drawn by our turtle
    b.right(angle)
    b.forward(140)
    b.backward(140)
    b.left(angle)

    # draw Second Hand
    angle = s * 6 - 90
    c.clear()  # clear previous drawings drawn by our turtle
    c.right(angle)
    c.forward(170)
    c.backward(170)
    c.left(angle)

    # tick every 1 second
    time.sleep(1)
    # if 1 - (time.time() - starttime) > 0:
    #    time.sleep(1 - (time.time() - starttime))


wn.exitonclick()
