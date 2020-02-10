from integrator import integrate
from numpy_integrator import numpy_integrate

def f(x):
    return x**2

print(integrate(f, 0, 1, 10000))
print(numpy_integrate(f, 0, 1, 10000))
