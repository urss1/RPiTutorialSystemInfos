# **************************************************
# My first Python Project
# 26.10.2018 V1.0 - sumali - Create Project
# **************************************************

# Imports
import sys
import platform
import os
import socket
import fcntl
import struct
import io.consolePrinter as console
import io.infoPrinter as printer

# Verschiedene Module und Funktionen
# --------------------------------------------------
def getCpuTemperature():
  try:
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
  except:
    return 0
    
def getIpAddress(network):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
      sock.fileno(),
      0x8915, # SIOCGIFADDR
      struct.pack('256s', network[:15])
    )[20:24])
  except:
    return "nicht verbunden"

def getOsVersionName():
  try:
    with open("/etc/os-release") as readFile:
      releaseInfos = dict()
      for line in readFile:
        key, value = line.rstrip().split("=")
        releaseInfos[key] = value.strip('"')
    return releaseInfos["PRETTY_NAME"]
  except:
    return "--"

# Der Haupteinstiegspunkt der Applikation
# --------------------------------------------------
def main(args):
  console.printInfo("SYSTEM-Uebersicht")
  
  printer.show("Betriebssystem", getOsVersionName())
  printer.show("Name des Pi", platform.node())
  printer.show("IP-Adresse (eth0)", getIpAddress('eth0'))
  printer.show("IP-Adresse (wlan0)", getIpAddress('wlan0'))
  print("")
  console.printInfo("SYSTEM-Informationen")
  printer.show("CPU-Temperatur", getCpuTemperature())
  
  return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))


