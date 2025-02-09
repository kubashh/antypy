from time import time

from values import white
from functions import cleanScreen, refreshScreen, drawText


class Engine:
  toUpdate = []
  toRender = []
  scene = False

  def setScene(scene):
    Engine.scene = scene
    Engine.render(0.0)

  def update(mouse):
    start = time()

    flag = False
    for arr in Engine.toUpdate:
      (a, b, c, d) = arr[0]
      if a < mouse[0] < a + c and b < mouse[1] < b + d:
        flag = True
        if arr[2] == False:
          arr[1]()
        elif arr[3] == False:
          arr[1](arr[2])
        else:
          arr[1](arr[2], arr[3])

    if flag:
      Engine.render(round(time() - start, 3))

  def render(lastUpdate):
    start = time()

    Engine.toUpdate.clear()
    cleanScreen()
  
    Engine.scene()
    
    for r in Engine.toRender:
      r()
    Engine.toRender.clear()
    
    drawText((0, 0), "Update: " + str(lastUpdate) + "s", white, 50, False, 8)
    drawText((0, 51), "Render: " + str(round(time() - start, 3)) + "s", white, 50, False, 8)

    refreshScreen()
