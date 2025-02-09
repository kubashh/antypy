from pygame import init, quit, event, QUIT, MOUSEBUTTONDOWN

from Engine import Engine
from menu.Menu import MenuScene

init()
Engine.setScene(MenuScene)

while True:
  ev = event.wait()
  if ev.type == MOUSEBUTTONDOWN:
    Engine.update(ev.pos)
  elif ev.type == QUIT:
    break
quit()