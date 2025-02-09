from random import shuffle

from values import gray, Game
from functions import chance, fromArr, fromColor



def prot(t):
  pt = 0
  if 10 < t.v <= 16:
    pt = min(5, t.v - 10)
  for t2 in t.n:
    if t2.color == t.color:
      tmp = min(5, t.v - 10)
      if pt < tmp:
        pt = tmp
  return pt



def move(p):
  for t in fromColor(p.color, True):
    if 10 < t.v <= 16:
      tmp = []
      for t2 in fromArr(t.n, True):
        if t2.color == gray or (t2.color == p.color and t2.v == 0 and t2.fl < t.fl) or (t2.color != p.color and prot(t2) < t.v - 10 and chance(p.aggressiveness)):
          t2.moved = True
          t2.v = t.v
          t2.color = p.color
          t.v = 0
          break


def buyHome(p, t):
  cost = 4
  if 0 <= t.v < 10 and cost <= p.cash:
    t.v += 1
    p.cash -= cost


def buyUnit(p, t):
  if t.v == 0 or 10 < t.v < 16:
    cost = 10
    if t.v != 0:
      cost = 10 * (t.v - 9)
    if cost <= p.cash:
      if t.v == 0:
        t.v = 11
      else:
        t.v += 1
      p.cash -= cost



def buy(p):
  for t in fromColor(p.color, True):
    if t.v == 0:
      if 4 < t.fl and chance(p.eco):
        buyHome(p, t)
      elif t.fl < 4 and chance(1 - 0.25 * t.fl):
        buyUnit(p, t)
    elif t.v <= 10:
      buyHome(p, t)
    elif t.v <= 16 and chance(0.5):
      buyUnit(p, t)



def updateFrontLine(color, deep = 0):
  if deep == 0:
    for t in Game.map:
      t.fl = -1
      if t.color == color:
        flag = False
        for t2 in t.n:
          if t2.color != color:
            flag = True
            break
        if flag:
          t.fl = 0
  
  
  for t in fromColor(color):
    if t.fl == deep:
      for t2 in t.n:
        if t2.color == color and t2.fl == -1:
          t2.fl = deep + 1

  if deep < 10:
    updateFrontLine(color, deep + 1)
  else:
    for t in fromColor(color):
      if t.fl == -1:
        t.fl = 11



def addRemoveCash(p):
  # Cash Add
  for t in fromColor(p.color):
    if 9 < t.fl and 10 < t.v <= 16:
      t.v = 0
    p.cash += 1
    if 0 < t.v <= 10:
      p.cash += t.v
  # Remove
  flag = False
  for t in fromColor(p.color):
    if 10 < t.v:
      cost = 1 + (t.v - 10) ** 2
      if cost <= p.cash:
        p.cash -= cost
      else:
        p.cash = 0
        flag = True
        break
  if flag:
    for t in fromColor(p.color):
      if 10 < t.v <= 16:
        t.v = 0



def nextTurn():
  for t in Game.map:
    t.moved = False
  for p in Game.players:
    addRemoveCash(p)
    updateFrontLine(p.color)
    move(p)
    buy(p)
