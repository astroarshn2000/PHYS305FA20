#!/use/bin/env python

"""
Title: Print the prime factor decomposition of a given Integer

Solution to Problem Set 1, Problem 2
~ Arsh R. Nadkarni

To run:
python primefactor_1_2.py <int> (Eg: primefactor_1_2.py 32)

This code takes an integer as an argument from the terminal and subsequently prints out 
the prime factors of that input integer as a list, on a line, followed by the 
multiplicity of the prime factors in braces.

"""
# import libraries
import sys
import math

# construct the prime factor decomposition function
def prime_fact_dec():
	# take input as an argument from the terminal
	if len(sys.argv) != 2:
		print("Usage: {0:s} <int>".format(sys.argv[0]))
		exit()
	# check whether the input argument is an integer or not
	try:
		num = int(sys.argv[1])
	except ValueError:
		print("Whoops! n is not an integer!")
		exit()  # 
    # define the input integer argument
	num = int(sys.argv[1])
	# method to find prime factors 
	for foo in range(2, int(math.sqrt(num)) + 1): # for loop on the integer range
		# check if num is a prime number
		init = 0 # initial counter variable 
		while num%foo == 0: # num is a prime number if num%foo==0
			init+=1         # iterate the counter variable
			num = num/foo   # update num
		# if num satisfies num%foo==0, output num
		if init != 0:
			print(" " + str(foo), end = "")
		# output the divisibility of the prime factor
		if init > 1:
			print("{" + str(int(init)) + "}", end = " ")
	# output the last num
	if num > 2:
		print(" " + str(int(num)), end = "")
	# print new line
	print()

prime_fact_dec() # call the function
