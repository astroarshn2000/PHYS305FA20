#!/usr/bin/env python
"""
Find root by bisection, animating progress

Problem set 1, problem 3

To run:
./bisection_anim_3_1.py

"""

import matplotlib.pyplot as plt
import numpy as np

def bisection(func, low, high, eps):
    """
    Find the root on the interval [low, high] to the tolerance eps
    ( eps apples to both function value and separation of the bracketing values )
    """

    # make plot of function
    fig, ax = plt.subplots()
    xvec = np.linspace(low, high)
    ax.plot(xvec, f(xvec))
    ax.plot([low, high], [0,0], 'r')

    # if bracket is backwards, swap values
    if low > high:
        low, high = high, low

    flow = func(low)
    fhigh = func(high)
    if flow*fhigh > 0:
        print("root is not bracketd by [", low, ", ", high,"]")
        exit(1)

    mid = 0.5*(high+low)
    fmid = func(mid)

    # add points at low, mid, and high
    lowpt, = ax.plot(low, flow, 'ro')
    midpt, = ax.plot(mid, fmid, 'bo')
    highpt, = ax.plot(high, fhigh, 'ro')

    while (high-low) > eps and abs(fmid)>eps:

        plt.pause(1)

        if fmid*flow < 0:
            high = mid
            fhigh = fmid
            # remove high point and replace it
            highpt.remove()
            highpt, = ax.plot(high, fhigh, 'ro')
        else:
            low = mid
            flow = fmid
            # remove low point and replace it
            lowpt.remove()
            lowpt, = ax.plot(low, flow, 'ro')

        mid = 0.5*(high+low)
        fmid = func(mid)

        # remove mid point and replace it
        midpt.remove()
        midpt, = ax.plot(mid, fmid, 'bo')

        print(mid)

    return mid

def f(x):
    return np.tan(x) - 3

low = 0.7
high = 1.5

epsilon = 1e-4
ans = bisection(f, low, high, epsilon)
print("root is at " , ans)

plt.show()
