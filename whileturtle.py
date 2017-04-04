#draw.py example
import turtle 

painter = turtle.Turtle()
a = painter.pos()
a = map(float,a)
b = tuple()
c = 0
while map(float,b) != map(float,a):
	painter.forward(100)
	painter.left(75)
	b = map(float,painter.pos())
	c += 1
	print b
	print c

turtle.done()
