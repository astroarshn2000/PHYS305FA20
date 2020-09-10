#!/usr/bin/env python
"""
Print specified number of dots to the terminal

Problem set 1, problem 1

To run:
./dots_1_1.py

"""

s = input("enter an integer: ")

# check that input converts correctly to an integer
try:
    m = int(s)
except ValueError:
    print("that was not an integer")
    exit(1)

dots = "."*m  # make a string of m dots
print(dots)

"""
or, you could do something like:

for i in range(m):
   print(".", end="")
print()

"""
