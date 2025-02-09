from pygame import draw, display, font, Surface, SRCALPHA
from random import random, choice, shuffle

from values import screen, white, black, colors, Game


# Draw

def drawText(pos, text, color = white, textSize = 50, center = False, p = -1):
  (x, y) = pos
  fnt = font.SysFont(None, textSize)
  text = fnt.render(text, True, color)
  w = text.get_width()
  h = text.get_height()
  if center:
    x -= 0.5 * w
    y -= 0.5 * h
  if p != -1:
    drawTransparentBox((x - p, y - p, w + 2 * p, h + 2 * p), (0, 0, 0, 127))
  screen.blit(text, (x, y))


def drawBox(pos, color):
  draw.rect(screen, color, pos)


def drawTransparentBox(pos, color):
  s = Surface((pos[2], pos[3]), flags=SRCALPHA)
  s.fill(color)
  screen.blit(s, (pos[0], pos[1]))


def drawPolygon(pos, color):
  draw.polygon(screen, color, pos)


def cleanScreen():
  screen.fill(black)


def refreshScreen():
  display.update()



# Math

def chance(a):
  if random() < a:
    return True


def randUnusedColor():
  color = choice(colors)
  for p in Game.players:
    if p.color == color:
      return randUnusedColor()
  return color



def fromArr(arr, rand = False):
  arr2 = []
  for t in arr:
    arr2.append(t)
  if rand:
    shuffle(arr2)
  return tuple(arr2)


def fromColor(color, rand = False):
  arr = []
  for t in Game.map:
    if t.color == color:
      arr.append(t)
  if rand:
    shuffle(arr)
  return tuple(arr)
