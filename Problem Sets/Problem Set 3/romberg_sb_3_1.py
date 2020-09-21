#!/usr/bin/env python

"""
Title: Solving the Given Integral and Numerically calculating Stefan-Boltzmann Constant using Romberg Integration.

Solution to Problem Set 3, Problem 1
~ Arsh R. Nadkarni

To run:
python romberg_sb_3_1.py

- Can change the no. of points by changing N in romberg()
- Can change the tolerance by changing eps in romberg_sb()

"""
# import libraries
from math import exp, pi, sqrt
import numpy as np

# construct trapezoid-rule ftion (taken from pseudo-code)
def trap(f, a, b, n):
    N = 2**n
    n = np.linspace(1, N//2, N//2)
    h = (b-a)/N
    In = 0
    for i in n:
        In = In + f(a + (2*i - 1)*h)
    return h*In

# construct romberg integrator function (taken from pseudo-code)
def romberg(f, a, b, eps):
    N = 30               # no. of points that make up the smaller intervals
    h = (b-a)/(N-1)      # length of each small interval    
    I = []
    foo = []
    foo.append(1/2*(b - a)*(f(a) + f(b)))
    I.append(foo)
    for n in range(1, N):
        foo = []
        foo.append(0.5*I[n - 1][0] + trap(f, a, b, n))
        for k in range(1, n + 1):
            q = 4**k
            foo.append((q*foo[k - 1]-I[n-1][k-1])/(q - 1))
        I.append(foo)
        if(abs(I[n][n] - I[n][n - 1]) < eps * I[n][n - 1]):
            return I[n][n]
    print("Failure to converge!")

# construct a function to get an answer to the integral and find sigma
def romberg_sb():
    # define the function to be integrated and account for dividing by zero
    def f(x):
        if((exp(x) - 1) == 0):
            return 0
        else:
            return x**3/(exp(x) - 1)
    # function arguments and integration limits
    a = 0       # lower limit (0)
    b = 100     # upper limit (inf.)
    eps = 1e-5  # error tolerance
    # calculate the value of the integral without the constants
    sb_init = romberg(f, a, b, eps)
    print("The Value of the Integral using Romberg Integration is = ", sb_init)
    # calculate the Stefan-Boltzmann constant by adding in the value of all the initial constants
    cons = 114531559.123
    sbc = sb_init/cons
    print("The Value of the Stefan-Boltzmann Constant = ", sbc, end=" ")
    print("W*m^-2*K^-4")
romberg_sb()
