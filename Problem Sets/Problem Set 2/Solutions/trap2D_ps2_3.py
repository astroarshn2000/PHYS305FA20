"""
    2D trapezoidal rule to integrate Gauss's law for a dipole

    Solution to Problem Set 2, Problem 3
    To run:
        python trap_rule_2_3.py

"""

import matplotlib.pyplot as plt
import numpy as np

def trap_2D(f, x_min, x_max, y_min, y_max, n, m,*P):
    hx = (x_max-x_min)/n
    hy = (y_max-y_min)/m

# contributions from rectangle corners
    I = (f(x_min,y_min,*P)+f(x_min,y_max,*P)+f(x_max,y_min,*P)+f(x_max,y_max,*P))/4


# contributions from rectangle sides
    I_x = 0

    for i in range(1,n):
        xi = x_min+i*hx
        I_x += (f(xi,y_min,*P)+f(xi,y_max,*P))/2;

    I_y = 0

    for j in range(1,m):
        yj = y_min+j*hy
        I_y += (f(x_min,yj,*P)+f(x_max,yj,*P))/2

# contributions from inside of rectangle
    I_xy = 0

    for i in range(1,n):
        for j in range(1,m):
            xi = x_min+i*hx
            yj = y_min+j*hy

            I_xy += f(xi,yj,*P)

    return (I+I_x+I_y+I_xy)*hx*hy


#function to be integrated, divided by q
def Er_R2_overQ(theta,phi, d,R):
    return 1/(4.*np.pi) * (2+d/R*np.sin(theta)*np.cos(phi))*np.sin(theta)


int_analytic = 2.0
#integration boundaries
theta_min = 0
theta_max = np.pi
phi_min = 0
phi_max = 2.*np.pi
#choose some values for (d,R) such that d/R = 0.1
d = 0.1
R = 1
P =(0.1,1)
N = np.array([50, 100, 200, 400])
rel_err = np.zeros(4)
for i in range(N.shape[0]):
    int_trap = trap_2D(Er_R2_overQ, theta_min,theta_max,phi_min,phi_max, N[i], N[i],*P)
    rel_err[i] = np.abs(int_trap - int_analytic) / int_analytic

#fit a line to log(N), log(rel_err) to get slope/convergence rate
m, b = np.polyfit(np.log(N), np.log(rel_err), 1)
print("convergence rate 2D trapezoidal rule %.3f" % m)
plt.xlabel("log(number of steps)")
plt.ylabel("log(relative Error)")
plt.yscale('log')
plt.xscale('log')
#plot relative error
plt.plot(N, rel_err, marker ='o',label='2D Trapezoidal Rule',color ='b')
# and best fit
plt.plot(N,np.exp(np.log(N)*m+b),linestyle = "--",color ='b')
plt.legend()
plt.show()
