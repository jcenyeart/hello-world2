#custom shape
import turtle 

a = input("How many sides?")
b = input("How many interations")

painter = turtle.Turtle()
for j in range(b):
	for _ in range(a):
		painter.forward(100-10*j)
		painter.left(180 - 180*(a-2)/(a))

turtle.done()