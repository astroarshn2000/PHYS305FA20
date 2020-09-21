"""
Title: Numerically Integrating f(x) = xe^(-ax) using the One-dimensional Trapezoidal Method

Solution to Problem Set 2, Problem 1
~ Arsh R. Nadkarni

To run:
python trapezoidal_2_1.py

"""
# import libraries
import numpy as np
from math import exp
import matplotlib.pyplot as plt

# function to be integrated (integrand)
def f(x):
    return x*np.exp(-1*2*x)

# construct the trapezoidRule function based on the pseudo-code in ProblemSet2.pdf
def trapezoidalRule(func,a,b,n):
    h = (b-a)/n
    I1 = func(a) + func(b)
    I2 = 0
    i = 1
    for i in range(1,n):
        x = a+i*h
        I2 += f(x)
        i += 1
    I = (h/2)*(I1+(2*I2))
    return I

# function to return the value for the definite integral at n=100 (Problem 1 - Part 1)
def A():
    answer = trapezoidalRule(f, 0, 1, 100)
    print("The value of the integral computed using the Trapeizodal Rule is", answer)
A()

# function to evaluate the error and plot the relative error as a function of n on a log-log plot, comparing it with the expected order of convergence (Problem 1 - Part 2)
def B():
    t = 4
    N = np.zeros(t)
    err = np.zeros(t)
    I = np.zeros(t)
    aval = 0.1484985375725405 # analytical value of the integral
    for i in range(t):
        n = 50 * (2**i) # n= 50,100,200,400
        N[i] = n
        I[i] = trapezoidalRule(f, 0, 1, n)
        err[i] = np.abs((aval-I[i])/I[i])
    fig,a = plt.subplots(figsize=(10,8))
    a.loglog(N,err,'r--',label='Relative Error',lw=3)
    a.loglog(N,1/N**2,'b-',label='Expected Convergence (1/$n^2$)',lw=3)
    a.set_xlabel('log(n)',fontweight='bold')
    a.set_ylabel('log(Relative Error)',fontweight='bold')
    plt.legend()
    plt.title('Relative Error as a function of n: log-log Plot (Case: i=1,..,n-1)', fontweight='bold')
    plt.show()
B()

# function to find an approximate n such that the numerical answer is accurate to at least five significant figures (Problem 1 - Part 3)
def C():
    aval = 0.1484985375725405 # analytical value of the integral (Calculated by Hand)
    eps = 1e-5 # tolerance of 5 significant figures
    n = 1
    while n < 1000:
        I = trapezoidalRule(f, 0, 1, n)
        err = abs((I-aval)/I)
        if err < eps:
            print("Approx. n such that numerical answer is accurate to at least 5 significant figures is", n)
            n = 1001
        else:
            n += 1
C()

# construct the trapezoidRule function to iterate i to n instead of n-1
def trapezoidalRule_n(func,a,b,n):
    h = (b-a)/n
    I1 = func(a) + func(b)
    I2 = 0
    i = 1
    for i in range(0,n+1):
        x = a+i*h
        I2 += f(x)
        i += 1
    I = (h/2)*(I1+(2*I2))
    return I

# function to evaluate the error and plot the relative error as a function of n on a log-log plot, comparing it with the expected order of convergence (Problem 1 - Part 2)
def D():
    t = 4
    N = np.zeros(t)
    err = np.zeros(t)
    I = np.zeros(t)
    aval = 0.1484985375725405 # analytical value of the integral (Calculated by Hand)
    for i in range(t):
        n = 50 * (2**i) # n= 50,100,200,400
        N[i] = n
        I[i] = trapezoidalRule_n(f, 0, 1, n)
        err[i] = np.abs((aval-I[i])/I[i])
    fig,a = plt.subplots(figsize=(10,8))
    a.loglog(N,err,'r--',label='Relative Error',lw=3)
    a.loglog(N,1/N**2,'b-',label='Expected Convergence (1/$n^2$)',lw=3)
    a.set_xlabel('log(n)',fontweight='bold')
    a.set_ylabel('log(Relative Error)',fontweight='bold')
    plt.legend()
    plt.title('Relative Error as a function of n: log-log Plot (Case: i=0,..,n) ', fontweight='bold')
    plt.show()
D()

"""
The order of convergence does not match the expected order (O(1/n^2)) and we obtain a slope in the plot which is equal to −1.
This is likely because in part D) we are iterating i from 0,..,n which means the function is integrated at both its endpoints,
thus increasing the value of the approximation and the errors corresponding to each n.

"""

