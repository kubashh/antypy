import pygame

from values import screen, white, gray, width, Game
from functions import drawText
from Button import Button
from Engine import Engine
from game.nextTurn import nextTurn
from game.drawMap import drawMap


class Info:
  s = False
  def show():
    Info.s = not Info.s

  def draw():
    for i in range(0, len(Game.players)):
      p = Game.players[i]
      drawText((20, 140 + i * 60), f"Player {i}, Cash {p.cash}, Aggressivenness {p.aggressiveness}, Economic {p.eco}", white, 50, False, 12)


def GameScene():
  drawMap()
  
  if Info.s:
    Info.draw()

  w = width // 2
  y = -160
  # Next turn button
  s = "Show info"
  if Info.s:
    s = "Hide info"
  Button((0, y, w, 0), gray, s, Info.show)
  Button((w, y, 0, 0), gray, "Next turn", nextTurn)
