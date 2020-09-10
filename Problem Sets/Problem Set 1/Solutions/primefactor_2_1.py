#! /usr/bin/env python
"""
Prime factorization by brute force

Problem set 1, problem 2

To run:
./primefactor_2_1.py <positive integer>

"""
import sys

def primefactor(n):
    """
    print the prime factorization of n
    """

    # must have positive integer
    assert n > 0

    # try all possible divisors
    # NB that if factor is not a prime, we will have divided by its
    # prime factors already and we will simply move on...
    factor = 2     # starting with 1 will end badly...
    while n > 1:
        multiplicity = 0
        while n%factor == 0:
            multiplicity += 1
            n = n//factor   # don't forget to use integer division

        if multiplicity > 1:
            # either of these two print statements will do...
            # remember, to get a "{" or a "}" in the output, one has to double it
            print("{:d}{{{:d}}} ".format(factor,multiplicity), end="")
            # here we get rid of the extra spaces by using sep=""
            #print(factor, "{", multiplicity,"} ", sep="", end="")
        elif multiplicity == 1:
            print("{:d} ".format(factor), end="")

        factor += 1

    print()

def Usage():
    print("Usage: {0:s} <positive integer>".format(sys.argv[0]))
    exit()

if len(sys.argv)!=2:
   Usage()

try:
   n = int(sys.argv[1])
except ValueError:
   print(sys.argv[1], "is not an integer")
   Usage()

if n < 1:
    print(n, "is not a positive integer")
    Usage()

primefactor(n)
