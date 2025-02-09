class Tile:
  __slots__ = "moved", "x", "y", "v", "fl", "color", "n"
  def __init__(self, x, y, c):
    self.moved = False
    self.x = x
    self.y = y
    self.v = 0
    self.fl = 0
    self.color = c
    self.n = ()
