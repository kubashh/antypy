from values import width, height, white, black
from functions import drawText, drawBox
from Engine import Engine



def Button(pos, color, text, f = False, arg = False, arg2 = False):
  (a, b, c, d) = pos

  c -= a
  d -= b

  if a < 0:
    a = width + a
  if c <= 0:
    c = width + c
  if b < 0:
    b = height + b
  if d <= 0:
    d = height + d
  
  pos = (a, b, c, d)

  if f:
    Engine.toUpdate.append((pos, f, arg, arg2))


  drawBox(pos, black)
  if color != black:
    m = 6
    pos2 = (a + m, b + m, c -  2 * m, d - 2 * m)
    drawBox(pos2, color)

  drawText((a + c * 0.5, b + d * 0.5), text, white, 50, True)
