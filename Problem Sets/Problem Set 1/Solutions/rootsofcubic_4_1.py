#!/usr/bin/env python
"""
Find all of the roots of x^3 - 25 x^2 + 165 x - 275 by
combined bisection/Newton method

Problem set 1, problem 4

To run:
./rootsofcubic_3_1.py

"""
import matplotlib.pyplot as plt
import numpy as np
from rtsafe import rtsafe

# function returns its value and its derivative
def f(x):
    ff = x**3 - 25*x**2 + 165*x - 275
    df = 3*x**2 - 50*x + 165
    return ff, df

fig,ax = plt.subplots()
x = np.linspace(-5, 25, 100)
y, dy = f(x)
ax.plot(x, y)
ax.plot([-5,25],[0,0],'r')
plt.pause(0.1)

for i in range(3):
    inp = input("enter low, high bracket for root: ")
    inp1, inp2 = inp.split()
    try:
        low = float(inp1)
    except ValueError:
        print(inp1, "is not numeric value")
        exit()
    try:
        high = float(inp2)
    except ValueError:
        print(inp2, "is not numeric value")
        exit()

    ans = rtsafe(f, low, high, 1e-10)
    if ans == None:
        print("Failed!")
    else:
        print("root on [",low,",",high,"] =",ans)
        y,dy = f(ans)
        ax.plot(ans,y,'ro')
        plt.pause(0.1)

plt.show()
