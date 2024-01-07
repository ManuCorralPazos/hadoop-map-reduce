#!/usr/bin/python3

import sys

for linea in sys.stdin:
  linea = linea.strip()
  persona, tienda, gasto = linea.split(";", 2)
  print("%s;%s;%s" % (persona, tienda, gasto))
