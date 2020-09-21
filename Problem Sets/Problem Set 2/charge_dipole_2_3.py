"""
Title: Finding the Total Charge of an Equal Charge Electric Dipole using the Two-dimensional Trapezoidal Method

Solution to Problem Set 2, Problem 3
~ Arsh R. Nadkarni

To run:
python charge_dipole_2_3.py

"""
# import libraries
import math
import numpy as np
import matplotlib.pyplot as plt

def totalcharge(n):
    # function to be integrated (integrand)
    def f(theta,phi):
        return 2*np.sin(theta)+0.1*np.cos(phi)*(np.sin(theta))**2
    # construct the trapezoidRule function based on Problem 2
    def trapezoidalRule(f,n):
        a = 0
        b = 2*np.pi
        c = 0
        d = np.pi
        hx = (b - a)/n
        hy = (d - a)/n
        I1 = f(a, c) + f(b, d)
        I2 = 0
        i = 0
        j = 0
        for i in range (n+1):
            for j in range (n+1):
                x = a + (i * hx)
                y = a + (j * hy)
                I2 += f(x, y)
                i += 1
                j += 1
        I = ((hx/2) * (hy/2) * (I1 + (2 * I2)))
        return I
    # function to return the total charge
    def answer(f,n):
        q=1.60217662*1e-19
        global ans
        ans=(q/(4*np.pi))*(trapezoidalRule(f,n))
        return ans
    return answer(f,n)

# function to evaluate the error and plot the relative error as a function of n on a log-log plot, comparing it with the expected order of convergence
def B():
    t = 4
    N = np.zeros(t)
    err = np.zeros(t)
    I = np.zeros(t)
    aval = -1.56*1e-19 # analytical value of the integral (Calculated by Hand)
    for i in range(t):
        n = 50 * (2**i) # n= 50,100,200,400
        N[i] = n
        I[i] = totalcharge(n)
        err[i] = abs(aval-I[i])
    figure,a = plt.subplots()
    a.loglog(N,err,'r--',label='Relative Error',lw=3)
    a.loglog(N,1/N**2,'b-',label='Expected Convergence (1/$n^2$)',lw=3)
    a.set_xlabel('log(n)',fontweight='bold')
    a.set_ylabel('log(Relative Error)',fontweight='bold')
    plt.legend()
    plt.title('Relative Error as a function of n: log-log Plot', fontweight='bold')
    plt.show()
    figure,b = plt.subplots()
    b.plot(N,err,'r--',label='Relative Error',lw=3)
    b.plot(N,1/N**2,'b-',label='Expected Convergence (1/$n^2$)',lw=3)
    b.set_xlabel('n',fontweight='bold')
    b.set_ylabel('Relative Error',fontweight='bold')
    plt.legend()
    plt.title('Relative Error as a function of n', fontweight='bold')
    plt.show()
B()

"""
The value obtained numerically converges to the expected result (O(1/n^2)) at n = 400 approximately.
This can be verified using the plots above.

"""