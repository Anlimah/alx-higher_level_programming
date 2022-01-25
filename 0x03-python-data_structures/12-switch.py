#!/usr/bin/python3
a = 89
b = 10
tmp = b, b = a, a = tmp
print("a={:d} - b={:d}".format(a, b))
