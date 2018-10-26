# **************************************************
# io/consolePrinter
# 26.10.2018 V1.0 - sumali - Create Project
# **************************************************
def printInfo(message):
  _printOnConsole("INF", message)

def printError(message):
  _printOnConsole("ERR", message)
  
def printWarning(message):
  _printOnConsole("WRN", message)

def _printOnConsole(prefix, string):
  print "{0}: {1}".format(prefix, string)
