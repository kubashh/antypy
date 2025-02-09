from values import Game
from functions import randUnusedColor


class Player:
  __slots__ = "color", "tiles", "cash", "aggressiveness", "eco"
  def __init__(self):
    self.color = randUnusedColor()
    self.tiles = []
    self.cash = 20
    self.aggressiveness = 0.5
    self.eco = 0.5

    Game.players.append(self)
