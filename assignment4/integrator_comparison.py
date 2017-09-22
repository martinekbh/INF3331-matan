from numpy import sin, pi
from integrator import midpoint_integrate
from numpy_integrator import numpy_midpoint_integrate
from numba_integrator import numba_midpoint_integrate

N = 10**(7)
"""
jump=10**(6)
for n in range(100, N, jump):
    I = midpoint_integrate(sin, 0, pi, n)
    print(I)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be at least %d to have an error less than 10^(-10) \nwhen integrating with midpoint_integrate" % (n))
        break
    else:
        if n >= N-jump:
            print("Didn't find a large enough N")
"""

for n in range(128200, N, 1):
    I = numpy_midpoint_integrate(sin, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be at least %d to have an error less than 10^(-10) \nwhen integrating with numpy_midpoint_integrate" % (n))
        print("I = %f" % (I))
        break
    else:
        if n >= N-1:
            print("Didn't find a large enough N")

for n in range(128200, N, 1):
    I = numba_midpoint_integrate(sin, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be at least %d to have an error less than 10^(-10) \nwhen integrating with numba_midpoint_integrate" % (n))
        print("I = %f" % (I))
        break
    else:
        if n >= N-1:
            print("Didn't find a large enough N")

