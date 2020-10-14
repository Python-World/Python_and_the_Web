import turtle
import time

wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("Analogue Clock")
wndw.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hands
    # Each tuple in list hands describes the color, the length
    # and the divisor for the angle
    hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])


while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()

wndw.mainloop()
