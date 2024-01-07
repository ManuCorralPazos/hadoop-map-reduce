#!/usr/bin/python3

import sys

subproblema = None
sumaGasto = None
count = None

for claveValor in sys.stdin:
  persona, tienda, gasto = claveValor.split(";", 2)
  gasto = float(gasto)
  if subproblema == None:
    subproblema = [persona, tienda]
    sumaGasto = 0
    count = 0
  if subproblema == [persona, tienda]:
    sumaGasto += gasto
    count += 1
  else:
    print("%s;%s;%s;%s" % (subproblema[0], subproblema[1], sumaGasto, count))
    subproblema = [persona, tienda]
    sumaGasto = gasto
    count = 1
print("%s;%s;%s;%s" % (subproblema[0], subproblema[1], sumaGasto, count))