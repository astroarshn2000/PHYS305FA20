"""
Evaluate the integral of x * exp(-a * x) with a = 2 on [0,1].
    Determine the relative error as a function of step size N and
    find N such that the approximate integral isaccurate to
    five significant digits

Solution to Problem Set 2, Problem 1

To run:
    python trap_rule_2_1.py

"""

import numpy as np
import matplotlib.pyplot as plt

#original trapezoidal rule; loop from 1 to n - 1
def trapezoidalRule(func, a, b, n, *P):
        h = (b - a) / n
        Int_part1 = func(a, *P) + func(b, *P)
        Int_part2 = 0
        for i in range(1, n):
            x = a + i * h
            Int_part2 += func(x, *P)
        I = (h / 2) * (Int_part1 + 2 * Int_part2)
        return I
#for part 4 of problem 1: modify step d to loop from 0 to n
def trapezoidalRule_modified(func, a, b, n, *P):
        h = (b - a) / n
        Int_part1 = func(a, *P) + func(b, *P)
        Int_part2 = 0
        for i in range(0, n+1):
            x = a + i * h
            Int_part2 += func(x, *P)
        I = (h / 2) * (Int_part1 + 2 * Int_part2)
        return I

#the function to be integrated
def integrand(x,alpha):
    return x*np.exp(-alpha*x)
#the indefinite integral
def int_indef(x,alpha):
    return ((-x/alpha) - (1./alpha**2)) * np.exp(-alpha*x)

alpha = 2.0
#integral boundaries
xmax = 1.0
xmin = 0.0

#analytic result
int_analytic = int_indef(xmax,alpha)-int_indef(xmin,alpha)
#build the n vs relErr arrays
N = np.array([50, 100, 200, 400])
rel_err = np.zeros(4)
for i in range(N.shape[0]):
    int_trap = trapezoidalRule(integrand, xmin, xmax, N[i], alpha)
    rel_err[i] = np.abs(int_trap - int_analytic) / int_analytic


#fit a line to log(N), log(rel_err) to get slope/convergence rate
m, b = np.polyfit(np.log(N), np.log(rel_err), 1)
print("convergence rate regular trapezoidal rule %.3f" % m)
plt.xlabel("log(number of steps)")
plt.ylabel("log(relative Error)")
plt.yscale('log')
plt.xscale('log')
#plot relative error
plt.plot(N, rel_err, marker ='x',label='Regular Trapezoidal Rule',color ='b')
# and best fit
plt.plot(N,np.exp(np.log(N)*m+b),linestyle = "--",color ='b')

#recalcuate the n and relErr arrays, but with the modified step d
rel_err_mod = np.zeros(4)
for i in range(N.shape[0]):
    int_trap = trapezoidalRule_modified(integrand, xmin, xmax, N[i], alpha)
    rel_err_mod[i] = np.abs(int_trap - int_analytic) / int_analytic


#fit a line to log(N), log(rel_err) to get slope/convergence rate
m, b = np.polyfit(np.log(N), np.log(rel_err_mod), 1)
print("convergence rate modified trapezoidal rule %.3f" % m)

#plot results
plt.plot(N, rel_err_mod, marker ='o',label='Modified Trapezoidal Rule',color ='r')
# and best fit
plt.plot(N,np.exp(np.log(N)*m+b),linestyle = "--",color ='r')
plt.legend()
plt.show()

#find an n accurate to at least five significant digits
N_5 = 10
int_trap = trapezoidalRule(integrand, xmin, xmax, N_5, alpha)
print("finding N_5...")
while np.abs(int_trap - int_analytic) / int_analytic >= 5.e-6:
    N_5 += 1
    int_trap = trapezoidalRule(integrand, xmin, xmax, N_5, alpha)
#    print("\tN=%d\t I=%.7e\taccuracy=%.6e"%(N_5,int_trap,np.abs(int_trap - int_analytic) / int_analytic))
#print the results
print("Integration with N = %d has relative error %e\naccurate to at least 5 digits!"%(N_5,np.abs(int_trap - int_analytic) / int_analytic))
