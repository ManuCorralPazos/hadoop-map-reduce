#!/usr/bin/python3

import sys

subproblema = None
listaCitantes = None

for claveValor in sys.stdin:
  
  citada, citantes = claveValor.split("\t", 1)
  
  if subproblema == None:
    subproblema = citada
    listaCitantes = ""
    
  if subproblema == citada:
    listaCitantes = citantes
   
  else:
    print("%s\t%s" % (subproblema, listaCitantes))
    subproblema = citada
    listaCitantes = citantes

print("%s\t%s" % (subproblema, listaCitantes))