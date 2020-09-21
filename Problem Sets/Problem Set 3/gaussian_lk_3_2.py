#!/usr/bin/env python

"""
Title: Solving Lord Kelvin's Integral using Romberg Integration.

Solution to Problem Set 3, Problem 2
~ Arsh R. Nadkarni

To run:
python gaussian_lk_3_2.py

- Can change the no. of points by changing N in romberg()
- Can change the tolerance by changing eps in lk()

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
def lk():
    # define the function to be integrated and account for dividing by zero
    def f(x):
        if((exp(x) - 1) == 0):
            return 0
        else:
            return exp(-1*(x**2))
    # function arguments and integration limits
    a = -100    # lower limit (-inf.)
    b = 100     # upper limit (inf.)
    eps = 1e-15  # error tolerance
    # calculate the value of the integral without the constants
    answer = romberg(f, a, b, eps)
    print("Value of Lord Kelvin's Integral =", answer)
lk()

"""
It is observed that as the error tolerance is increased (going from 1e-5 to 1e-15), 
the answer comes out to be even closer to the analytical value (1.77245). A MathError 
is encountered if the limits of integration are increased beyond 100. However, there
is definitely symmetry in the function to be integrated about y=0, so we can just 
integrate it from 0 to infinity (some large value) and multiply it by 2. This will add
the areas under the curve, which happen to be equal in this case.

"""
