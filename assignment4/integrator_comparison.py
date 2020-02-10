from numpy import sin, pi
from integrator import integrate, midpoint_integrate
from numpy_integrator import numpy_integrate, numpy_midpoint_integrate
from numba_integrator import numba_integrate, numba_midpoint_integrate

def f(x):
    return sin(x)

N = 10**(10)
jump=100

#FOR INTEGRATE
for n in range(100, N, jump):
    I = integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with integrate" % (n))
        break
    else:
        if n >= N-jump:
            print("Didn't find a large enough N")

#FOR MIDPOINT INTEGRATE
for n in range(100, N, jump):
    I = midpoint_integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with midpoint_integrate" % (n))
        break
    else:
        if n >= N-jump:
            print("Didn't find a large enough N")

#FOR NUMPY INTEGRATE
for n in range(100, N, jump):
    I = numpy_integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with numpy_integrate" % (n))
        #print("I = %f" % (I))
        break
    else:
        if n >= N-1:
            print("Didn't find a large enough N")

#FOR NUMPY MIDPOINT INTEGRATE
for n in range(100, N, jump):
    I = numpy_midpoint_integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with numpy_midpoint_integrate" % (n))
        #print("I = %f" % (I))
        break
    else:
        if n >= N-1:
            print("Didn't find a large enough N")

#FOR NUMBA INTERGATE
for n in range(100, N, jump):
    I = numba_integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with numba_integrate" % (n))
        print("I = %f" % (I))
        break
    else:
        if n >= N-jump:
            print("Didn't find a large enough N")


#FOR NUMBA MIDPOINT INTEGRATE
for n in range(100, N, jump):
    I = numba_midpoint_integrate(f, 0, pi, n)
    if abs(I - 2.0) < 10**(-10):
        print("N needs to be %d or higher to have an error less than 10^(-10) \nwhen integrating with numba_midpoint_integrate" % (n))
        print("I = %f" % (I))
        break
    else:
        if n >= N-jump:
            print("Didn't find a large enough N")

