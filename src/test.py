#!/usr/bin/python -tt

import sys

count = 10
i = 0
lista = [ 11, 12, 13, 24, 25, 26, 37, 38, 49]
raw = 'Some text message for a string test'
print raw.upper()
print "Number of:", count

def TextProcess(count):
  return "Result: " +  str(count)
print TextProcess(10)
while i < len(lista):
  print lista[i]
  i += 3
print "Ostatni ele listy", lista[len(lista)-1]
sys.exit(1)
