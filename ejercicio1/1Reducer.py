#!/usr/bin/python3

import sys

subproblema = None
gastoMedio = None
contador = None

for claveValor in sys.stdin:
  
  persona, tienda, sumaGasto, count = claveValor.split(";", 3)
  sumaGasto = float(sumaGasto)
  count = float(count)
  if subproblema == None:
    subproblema = [persona, tienda]
    contador = 0
    gastoMedio = 0
    
  if subproblema == [persona, tienda]:
    contador += count;
    gastoMedio = sumaGasto/contador
   
  else:
    print("%s;%s;%s" % (subproblema[0], subproblema[1], gastoMedio))
    subproblema = [persona, tienda]
    contador = count
    gastoMedio = sumaGasto / contador

print("%s;%s;%s" % (subproblema[0], subproblema[1], gastoMedio))
