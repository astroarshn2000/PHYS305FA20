#!/usr/bin/env python

import sys

def factorial(n):
    print("factorial(",n,")")
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


arg = int(sys.argv[1])
ans = factorial(arg)
print("{}! = {}".format(arg,ans))
