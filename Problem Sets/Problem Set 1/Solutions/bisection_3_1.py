#!/usr/bin/env python
"""
Find root by bisection

Problem set 1, problem 3

To run:
./bisection_problem3.py

"""

def bisection(func, low, high, eps):
    """
    Find the root on the interval [low, high] to the tolerance eps
    ( eps apples to both function value and separation of the bracketing values )
    """

    # if bracket is backwards, correct this
    if low > high:
        low, high = high, low  # standard way to swap two variables
        # other way:
        #tmp = low
        #low = high
        #high = tmp

    flow = func(low)
    fhigh = func(high)
    if flow*fhigh > 0:
        print("root is not bracketd by [", low, ", ", high,"]")
        exit(1)

    mid = 0.5*(high+low)
    fmid = func(mid)

    while (high-low) > eps and abs(fmid)>eps:
        if fmid*flow < 0:
            high = mid
            fhigh = fmid
        else:
            low = mid
            flow = fmid

        mid = 0.5*(high+low)
        fmid = func(mid)

    return mid

if __name__ == "__main__":

    from math import tan

    def f(x):
        return tan(x) - 3

    epsilon = 1e-10
    ans = bisection(f, 1.5, 0.5, epsilon)
    print("root is at " , ans)

    # assert fails with "AssertionError" if argument is not true
    assert abs(f(ans)) <= epsilon
    print("proof:", abs(f(ans)), "<", epsilon)
