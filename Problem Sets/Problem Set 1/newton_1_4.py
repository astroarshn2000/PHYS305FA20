"""
Title: Finding where the function f(x) = x^4 - 7x + 10 has its minimum and determining the minimum value of the function

Solution to Problem Set 1, Problem 4
~ Arsh R. Nadkarni

To run:
python newton_1_4.py

Can change initial guess (x0), tolerance (eps), and number of iterations (n) in the function call on line 37

"""
# import libraries
import numpy as np

# define f(x)
def f(x):
    return x**4-7*x+10
# define the first derivative of f(x) 
def derf(x):
    return 4*x**3-7
# construct the newton method function
def newton(x0,eps,n):
    init = 1 # initial counter variable
    inf_init = 1 # initial infinite loop counter variable
    while True:
        xmin = x0 - f(x0)/derf(x0) # newton's method condition
        print('Iteration No-%d: xmin = %0.3f and f(xmin) = %0.3f' % (init, xmin, f(xmin)))
        x0 = xmin # update x0
        init += 1 # iterate the counter variable
        if init > n: # break the loop if it goes to infinite iterations
            inf_init = 0
            break
    print("Minimum:", np.min(xmin)) # print the minimum for the function
    print("The minimum value of f(x):", np.min(f(xmin))) # print the minimum value for the function

newton(3,1e-3,5) # call the function