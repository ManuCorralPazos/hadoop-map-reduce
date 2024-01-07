#!/usr/bin/python3

import sys

is_first_line = True

for linea in sys.stdin:
  linea = linea.strip()
    
  if is_first_line:
    is_first_line = False
    continue
    
  citante, citada = linea.split(",", 1)
  print("%s;%s" % (citada, citante))
