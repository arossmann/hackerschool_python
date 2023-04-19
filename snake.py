import turtle

import curses
import time

t = turtle.Turtle()
t.speed(0)
t.pensize(5)
t.color("red")

speed=5

screen = curses.initscr()
screen.keypad(True)
screen.nodelay(1)
while True:
  char = screen.getch()
  if char == 113: break  # q
  elif char == curses.KEY_RIGHT:
    t.right(90)
  elif char == curses.KEY_LEFT:
    t.left(90)
  elif char == curses.KEY_UP:
    t.forward(10)
  elif char == curses.KEY_DOWN:
    print("down\r\n")
  time.sleep(1/speed)
  t.forward(10)