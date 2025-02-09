from values import white, width, height, sq3, Game
from functions import drawText, drawPolygon



def drawTile(t):
  x = t.x * Game.pixelSize
  y = t.y * Game.pixelSize
  
  if not (0 < x < width and 0 < y < height):
    return

  w = Game.pixelSize * 0.5
  h = w * sq3

  drawPolygon([
    (x - w * 2, y),
    (x - w, y + h),
    (x + w, y + h),
    (x + w * 2, y),
    (x + w, y - h),
    (x - w, y - h)
  ], t.color)
  
  if t.v != 0:
    drawText((x, y), str(t.v), white, 50, True)


def drawMap():
  for t in Game.map:
    drawTile(t)
