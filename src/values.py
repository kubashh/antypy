from pygame import display, RESIZABLE
from math import sqrt

width = 1080
height = 2170

screen = display.set_mode((0, 0), RESIZABLE)

width, height = display.get_surface().get_size()


sq3 = sqrt(3)


class config:
  mapChance = 0.7
  mapSize = 5 * 3
  startingTileSize = 10
  maxPlayersCount = 8


class Game:
  pixelSize = 40
  screenCenter = (0, 0)
  map = []
  players = []



# Colors
black = (0, 0, 0)
darkGray = (63, 63, 63)
gray = (127, 127, 127)
lightGray = (167, 167, 167)
white = (255, 255, 255)

red = (255, 0, 0)
red2 = (127, 0, 0)
green = (0, 255, 0)
green2 = (0, 127, 0)
blue = (0, 0, 255)
blue2 = (0, 0, 127)

yellow = (255, 255, 0)
yellow2 = (127, 127, 0)
pink = (255, 0, 255)
pink2 = (127, 0, 127)
aqua = (0, 255, 255)
aqua2 = (0, 127, 127)


red4 = (63, 0, 0)
green4 = (0, 63, 0)
blue4 = (0, 0, 63)

red8 = (31, 0, 0)
green8 = (0, 31, 0)
blue8 = (0, 0, 31)


colors = [red, red2, green, green2, blue, blue2, yellow, yellow2, pink, pink2, aqua, aqua2]
