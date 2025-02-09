from time import time

from values import height
from functions import drawText, cleanScreen, refreshScreen


class Log:
  h = 40
  logs = []
  def add(text):
    Log.logs.append(text)
    if height < len(Log.logs) * Log.h:
      del Log.logs[0]
    Log.refresh()
  
  def editLast(text):
    Log.logs[-1] += text
    Log.refresh()
  
  def refresh():
    cleanScreen()

    i = 0
    for text in Log.logs:
      drawText((Log.h, i), text)
      i += Log.h
    
    refreshScreen()

  def time(text, f, arg = False):
    Log.add(text)
    start = time()
    if arg == False:
      f()
    else:
      f(arg)
    end = time()
    val = round(end - start, 3)
    Log.editLast(" (" + str(val) + "s)")
