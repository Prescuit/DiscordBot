def logMessage(msg):
  f = open("data/logs.txt", "a")
  f.write(msg)
  f.close()