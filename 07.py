import turtle
t = turtle.Turtle()

t = turtle.Turtle()
t.width(3)
t.shape("turtle")

def rechtwinkligesDreieck():
  t.up()
  t.goto(-300, 100)
  t.down()
  t.color("red")
  t.setheading(0)
  t.forward(60)
  t.left(90)
  t.forward(80)
  t.left(143)
  t.forward(100)

def gleichseitigesDreieck():
  t.up()
  t.goto(-200, 100)
  t.down()
  t.color("green")
  t.setheading(0)
  for i in [1, 2, 3, 4]:
    t.forward(60)
    t.left(120)

def Viereck():
  # Viereck
  t.up()
  t.goto(-100, 100)
  t.down()
  t.color("blue")
  t.setheading(0)
  for i in [1, 2, 3, 4]:
    t.forward(50)
    t.left(90)

def Kreis():
  # "Kreis"
  t.up()
  t.goto(0, 100)
  t.down()
  t.color('violet')
  for i in range(120):
    t.forward(1)
    t.left(3)
    t.forward(1)

rechtwinkligesDreieck()
gleichseitigesDreieck()
Viereck()
Kreis()