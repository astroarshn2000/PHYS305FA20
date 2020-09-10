#!/usr/bin/env python

"""
Title: Finding the root nearest to x=0 for f(x) = tan(x) - 3 using the Bisection Method

Solution to Problem Set 1, Problem 3
~ Arsh R. Nadkarni

To run:
python bfind_1_3.py

This code is a quantitative way to compute the midpoint of the function range initially and replace a or b, 
owing to the sign. The same is iterated until f(midpoint) is within the tolerance value (eps).
The upper limit (b), lower limit (a), and tolerance (eps) can be changed in the function arguments on line 51.

"""
# import libraries
import sys
import numpy as np

# define the function
def f(x):
    return np.tan(x) - 3
# find the root using the bisection method
def bisection(a,b,eps):
    # ensure that the a is negative and b is positive
	if f(a) > 0:
		a = b
		b = a
	elif f(a)*f(b) > 0: # check the validity of the bounds used
		print("Invalid Bounds. Root cannot be found!")
		exit()
	# define the mid-point
	mid = (a+b)/2
	# while loop to iterate the mid-point to until it is within eps
	while np.abs(f(mid)) >= eps:
		# update bounds
		if f(mid) >= 0:
			b = mid
		else:
			a = mid
		# calculate midpoint with updated bounds
		mid = (a+b)/2
	return mid
	
answer = bisection(-(np.pi/2),(np.pi/2),1e-3) # call the function

print("The root of f(x) = tan(x) - 3 nearest to x = 0 occurs at x =", answer) # print the answer