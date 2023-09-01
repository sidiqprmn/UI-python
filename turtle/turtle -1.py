import turtle

t = turtle.Turtle()

turtle.tracer(0)

t.pencolor("green")

for i in range(50):
  t.forward(i * 10)
  t.right(144)

  turtle.update()

  turtle.delay(10)

turtle.done()