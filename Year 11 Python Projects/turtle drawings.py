import turtle as pen
import math

def draw_circle_turning(x, y, radius, outline_color="blue", fill_color=None):
    pen.speed(0)
    pen.pensize(2)
    pen.color(outline_color)

    # Start at leftmost point so the center is (x, y)
    pen.penup()
    pen.goto(x - radius, y)
    pen.pendown()

    if fill_color:
        pen.fillcolor(fill_color)
        pen.begin_fill()

    # Move so total forward distance ≈ circumference
    step_len = (2 * math.pi * radius) / 360
    for _ in range(360):
        pen.forward(step_len)
        pen.left(1)

    if fill_color:
        pen.end_fill()

# --- Screen setup ---
screen = pen.Screen()
screen.setup(width=800, height=600, startx=100, starty=80)

# Example use
draw_circle_turning(40, 30, radius=100, outline_color="blue", fill_color="red")

screen.exitonclick()