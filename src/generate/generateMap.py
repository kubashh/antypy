from math import sqrt
from random import choice

from values import gray, config, Game
from functions import chance, fromColor
from generate.Tile import Tile
from generate.Log import Log



def refreshTiles():
  for i in range(0, len(Game.map)):
    t = Game.map[i]
    arr = []
    for j in range(max(0, i - config.mapSize * 2 - 3), min(i + config.mapSize * 2+ 3, len(Game.map))):
      t2 = Game.map[j]
      if t != t2 and sqrt((t.x - t2.x) ** 2 + (t.y - t2.y) ** 2) < 2:
        arr.append(j)
        if len(arr) == 6:
          break
    t.n = tuple(arr)

  

def generateMainShape():
  Game.map = []
  for x in range(0, config.mapSize * 2):
    for y in range(0, config.mapSize * 2):
      my = 0
      if x % 2 == 1:
        my = 0.9
      Game.map.append(Tile(x * 1.56, my + y * 1.8, gray))
  refreshTiles()



def plauge():
  arr = []
  for t in Game.map:
    arr.append([t.n])
  for i in arr[len(arr) // 2][0]:
    arr[i].append(True)
  for i in range(0, config.mapSize):
    for arr2 in arr:
      if len(arr2) < 2 or not arr2[1]:
        continue
      for i in arr2[0]:
        arr3 = arr[i]
        if len(arr3) < 2:
          arr3.append(False)
          if chance(config.mapChance):
            arr3[1] = True
  i = len(arr) - 1
  for arr2 in reversed(arr):
    if len(arr2) < 2 or not arr2[1]:
      del Game.map[i]
    i -= 1
  refreshTiles()
  Game.map = tuple(Game.map)



def intToPtr():
  for t in Game.map:
    arr = []
    for i in t.n:
      arr.append(Game.map[i])
    t.n = tuple(arr)



def setPlayer(color, deep = 0, size = config.startingTileSize):
  if size <= 0:
    return
  if 100 < deep:
    Log.add("ERROR!!!")
    return
  flag = False
  arr = []
  for t in fromColor(color):
    flag = True
    for t2 in t.n:
      if t2.color == gray:
        arr.append(t2)
  if flag and len(arr) == 0:
    # Clear
    for t in fromColor(color):
      t.color = gray
    setPlayer(color, deep + 1)
  for i in range(0, 100):
    if len(arr) == 0:
      t = choice(Game.map)
      if t.color == gray:
        arr.append(t)
  if len(arr) == 0:
    Log.add("ERROR 2!!!")
    return
  choice(arr).color = color
  setPlayer(color, deep + 1, size - 1)


def setPlayers():
  Game.players = tuple(Game.players)
  for p in Game.players:
    setPlayer(p.color)



def generateMap():
  Log.time("Generating main shape...", generateMainShape)
  Log.time("Plauge...", plauge)
  Log.time("Int to ptr...", intToPtr)
  Log.time("Setting players...", setPlayers)
  Log.add("Done, wait 1s to start")
