#!/usr/bin/python3

import sys

subproblema = None
listaCitantes = None

for claveValor in sys.stdin:
  citada, citante = claveValor.split(";", 1)
  
  if subproblema == None:
    subproblema = citada
    listaCitantes = ""

  if subproblema == citada:
    citante = citante.strip()
    listaCitantes += citante + ","

  else:
    print("%s\t%s" % (subproblema, listaCitantes))
    subproblema = citada
    citante = citante.strip()
    listaCitantes = citante + ","
    
print("%s\t%s" % (subproblema, listaCitantes))