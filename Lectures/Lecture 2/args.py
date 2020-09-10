#!/usr/bin/env python

import sys

nargs = len(sys.argv)

if nargs == 1:
    print("no args")
else:
    print(nargs-1,"args")
    for i in range(1,nargs):
        print("arg {} is {}".format(i,sys.argv[i]))
