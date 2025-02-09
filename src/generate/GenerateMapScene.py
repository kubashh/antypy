from time import sleep

from Engine import Engine
from game.Game import GameScene
from generate.generateMap import generateMap



def GenerateMapScene():
  generateMap()
  sleep(1)
  Engine.setScene(GameScene)
