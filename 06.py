import turtle

t = turtle.Turtle()
t.shape("circle")

farbe = input("bitte nenne mir eine Farbe:")

def farbiges_dreieck(farbe):
  t.up()
  t.goto(100,100)
  t.down()
  if farbe =="blau":
    t.color("blue")
  elif farbe =="rot":
    t.color("red")
  elif farbe =="grün":
    t.color("green")
  else:
    t.color("purple")
  t.setheading(0)
  t.forward(60)
  t.left(90)
  t.forward(80)
  t.left(143)
  t.forward(100)

def Kreis():
  # "Kreis"
  t.up()
  t.goto(-100, 100)
  t.down()
  t.color('violet')
  for i in range(120):
    t.forward(1)
    t.left(3)
    t.forward(1)

farbiges_dreieck(farbe)
Kreis()