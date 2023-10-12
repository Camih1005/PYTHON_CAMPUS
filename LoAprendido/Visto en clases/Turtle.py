import turtle
def dibLine(x1, y1, x2, y2):
  turtle.penup()


  turtle.goto(x1, y1)
  turtle.pendown()
  turtle.goto(x2, y2)

def EscrText(s, x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.write(s)


def EscrPunto(x, y):
   turtle.penup()
   turtle.goto(x,z)
   turtle.pendown()
   turtle.write(s)
   turtle.begin_fill()
   turtle.circle(3)
   turtle.end_fill()
   turtle.end_fill()


def EscCirulo(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def EscRectangulo(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
 