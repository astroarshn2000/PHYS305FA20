#!/usr/bin/env python
"""
Find minimum of x^4 - 7 x + 10
using Newton iteration on derivtive of function

Problem set 1, problem 5
Philip A. Pinto

To run:
./funcmin_5_1.py

"""
import matplotlib.pyplot as plt
import numpy as np

# function for which we want the minumum
def f(x):
    return x**4 - 7*x + 10

# function which returns derivative and second derivative of fullfunc
def df(x):
    ff = 4*x**3 - 7
    df = 12*x**2
    return np.array([ff, df])

def newton(func, xguess, epsilon):
    """
    Compute zero of func(x) with initial guess xguess
    func(x) must return function and its derivative
    """

    x = xguess
    MAXIT = 20
    for i in range(MAXIT):
        f, df = func(x)
        dx = - f/df
        if df == 0:
            print("newton: df = 0 at x = ", x)
            exit(1)
        x = x + dx
        if abs(dx) < epsilon or abs(f) < epsilon:break

    if i==MAXIT-1:
        print("newton failed to converge in ", i, " iterations")
        exit(1)

    return x

# plot the function, calling draw to show it immediately
fig, ax = plt.subplots()
x = np.linspace(-5, 5, 100)
ax.plot(x, f(x),'b')
plt.pause(0.1)

# get and sanity-check input
inp = input("enter guess for root: ")
try:
    low = float(inp)
except ValueError:
    print(inp, "is not numeric value")
    exit()

ans = newton(df, low, 1e-10)
if ans == None:
    print("Failed!")
else:
    print("minimum at x=",ans, "f=", f(ans), "df/dx=",df(ans)[0])

# plot a dot at the result
ax.plot(ans, f(ans),'ro')
plt.pause(0.1)

plt.show()
