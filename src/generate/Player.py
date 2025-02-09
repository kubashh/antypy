from values import Game
from functions import randUnusedColor


class Player:
  def __init__(self):
    self.color = randUnusedColor()
    self.tiles = []
    self.cash = 20
    self.aggressiveness = 0.5
    self.eco = 0.5

    Game.players.append(self)
