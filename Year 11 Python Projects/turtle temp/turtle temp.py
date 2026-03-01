import turtle as pen
import math

def circ(radius):
    step_len = (2 * math.pi * radius) / 360
    for _ in range(360):
        pen.forward(step_len)
        pen.left(1)
        
circ(100)