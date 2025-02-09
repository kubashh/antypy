from values import black, white, red, green8, width, config, Game
from functions import randUnusedColor, drawBox, drawText
from Button import Button
from Engine import Engine
from generate.GenerateMapScene import GenerateMapScene
from generate.Player import Player



def midVB(a, b, c, v, m):
  if m:
    v *= -1
  return sorted([a, b + v, c])[1]



def addPlayer(a = False, m = False):
  if m == False:
    if len(Game.players) < config.maxPlayersCount:
      Player()
  else:
    if 2 < len(Game.players):
      Game.players.pop()



def addMapSize(a = False, m = False):
  config.mapSize = midVB(3 * 3, config.mapSize, 15 * 3, 3, m)


def addMapChance(a = False, m = False):
  config.mapChance = midVB(0.4, config.mapChance, 0.9, 0.1, m)


def addAggressiveness(p, m = False):
  p.aggressiveness = midVB(0.1, p.aggressiveness, 0.9, 0.1, m)


def addEco(p, m = False):
  p.eco = midVB(0.1, p.eco, 0.9, 0.1, m)



def drawColumn(x, y, w, h, v, min, max, c):
  y += 6
  h -= 12
  y += h
  h *= (v - min) / (max - min)
  drawBox((x, y - h, w, h), c)



def doubleButtonPM(pos, color, v, min, max, f, arg = False):
  x, y, w, h = pos
  w3 = 20
  w2 = w * 0.5 - w3
  Button((x, y, x + w2, y + h), color, "-", f, arg, True)
  drawColumn(x + w2, y, w3, h, v, min, max, color)
  Button((x + w2 + w3, y, x + w, y + h), color, "+", f, arg)


def MenuScene():
  while len(Game.players) < 2:
    Player()

  h = 120
  y = 0

  # Draw title
  drawText((width * 0.5, h * 0.5), "Antypy", white, 80, True)
  y += h * 1.6

  w = width // 3
  # Labels
  drawText((w * 0.5, y + h * 0.5), "Players count", white, 50, True)
  drawText((w * 1.5, y + h * 0.5), "Map size", white, 50, True)
  drawText((w * 2.5, y + h * 0.5), "Map chance", white, 50, True)
  y += h

  # Functions
  doubleButtonPM((0, y, w, h), green8, len(Game.players), 2, 8, addPlayer, True)
  doubleButtonPM((w, y, w, h), green8, config.mapSize, 3 * 3, 15 * 3, addMapSize, True)
  doubleButtonPM((w * 2, y, w, h), green8, config.mapChance, 0.4, 0.9, addMapChance, True)
  y += h * 1.6

  # Players
  w = width // 3
  Button((0, y, w, y + h), black, "Players")
  Button((w, y, w * 2, y + h), black, "Aggressiveness")
  Button((w * 2, y, w * 3, y + h), black, "Enonomic")
  y += h

  for i in range(0, len(Game.players)):
    p = Game.players[i]
    def changeColor(p):
      p.color = randUnusedColor()
    Button((0, y, w, y + h), p.color, "Player " + str(i), changeColor, p)
    # Aggressiveness
    doubleButtonPM((w, y, w, h), p.color, p.aggressiveness, 0.1, 0.9, addAggressiveness, p)

    # Economic
    doubleButtonPM((w * 2, y, w, h), p.color, p.eco, 0.1, 0.9, addEco, p)
    y += h

  # Start game
  Button((200, -200, -200, 0), red, "Start", Engine.setScene, GenerateMapScene)
