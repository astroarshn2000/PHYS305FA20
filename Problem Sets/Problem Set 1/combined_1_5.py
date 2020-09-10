#!/usr/bin/env python

"""
Title: Determining all the roots for f(x) = x^3 - 25x^2 + 165x - 275 using the combined Bisection/Newton-Raphson Method

Solution to Problem Set 1, Problem 5
~ Arsh R. Nadkarni

To run:
python combined_1_5.py

Can change the x-range and tolerance (eps) on lines 103-105

This code computes the midpoint of the x-range initially and uses
Newton method to obtain the intersection of the function to the mid-point slope. 
If the value is in the range, it updates the lower-bound(a) or upper-bound(b),
owing to the sign. If not, the lower-bound(a) or upper-bound(b) is replaced with the mid-point.
The same procedure is iterated until the computed root is within the tolerance range.

"""
# import libraries
import sys
import numpy as np
import matplotlib.pyplot as plt

# construct function to find roots
def comb_root(a,b,eps):
    # define f(x)
	def f(x):
		return x**3 - 25*x**2 + 165 * x - 275
	# define the first derivative of f(x)
	def derf(x):
		return 3*x**2 - 50*x + 165 
	# ensure that the a is negative and b is positive
	if f(a) > 0:
		a = b
		b = a
	elif f(a)*f(b) > 0: # check the validity of the bounds used
		print("Invalid Bounds. Root cannot be found!")
		exit()
	# define the midpoint
	mid = (a+b)/2
	# begin newton iteration
	dxold = abs(b-a)
	dx = dxold
	fm = f(mid)
	dfm = derf(mid)
	# proceed until within the tolerance range
	while True:
		# condition for bisection/newton-raphson iteration
		if( (mid - b) * dfm - fm) * ( (mid - a) * dfm - fm) > 0 or abs(2*fm) > abs(dxold * dfm):
			dxold = dx
			dx = 0.5 * (b - a)
			mid = a + dx
		else:
			dxold = dx
			dx = fm/dfm
			mid = mid - dx
		# return mid if within in the tolerance range
		if (abs(dx) < eps): 
			return mid
		# calculate the function value and the first derivative value at the mid point
		fm = f(mid)
		dfm = derf(mid)
		# updates the bounds
		if fm < 0:
			a = mid
		else:
			b = mid

# function for confirming roots
def rc(root, rootName, eps):
    # define f(x)
	def f(x):
		return x**3 - 25*x**2 + 165 * x - 275
	# print confirmation of roots
	print(rootName + " computed as " + str(root))
	print("f(" + rootName + ") = " + str(f(root)))
	# check for tolerance of roots
	if np.abs(f(root)) <= eps:
		print("Root is within tolerance of " + str(eps))
	else:
		print("Root is not within tolerance of " + str(eps))

# function for outputting answers
def answers():
    # define f(x)
	def f(x):
		return x**3 - 25*x**2 + 165*x - 275
	# define the tolerance
	eps = 1e-3
	# Calculate all the roots using comb_root(a,b,eps)
	r1 = comb_root(2, 4, eps)
	r2 = comb_root(6, 8, eps)
	r3 = comb_root(15, 16, eps)
	# print and confirm roots
	rc(r1, "x1", eps)
	rc(r2, "x2", eps)
	rc(r3, "x3", eps)
	# create an array for x values 
	x = np.linspace(0, 20,1000)
	# plot f(x)
	plt.plot(x, f(x))
	plt.ylabel(r'$f(x)$', fontsize='large', fontweight='bold')
	plt.xlabel(r'$x$', fontsize='large', fontweight='bold')
	plt.ylim(-170, 60)
	plt.axhline(y=0, color='r', linestyle='-')
	plt.show()

answers() # call the function