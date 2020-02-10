from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate 
from integrator import integrate
import timeit

def f(x):
    return x**2


for N in [10**6, 10**7, 10**8]:
    #integrator time
    time=min(timeit.repeat(stmt="integrate(f, 0, 1, N)",
                    setup="from __main__  import f, integrate, N", repeat=5, number=5))
    print("Integrate for N = ", N, ": ", time)

    #numpy_integrator time
    numpytime=min(timeit.repeat(stmt="numpy_integrate(f, 0, 1, N)",
                    setup="from __main__  import f, numpy_integrate, N", repeat=5, number=5))
    print("Numpy for N = ", N, ": ", numpytime)

    #numba_integrator time
    numbatime=min(timeit.repeat(stmt="numba_integrate(f, 0, 1, N)",
                    setup="from __main__  import f, numba_integrate, N", repeat=5, number=5))
    print("Numba for N = ", N, ": ", numbatime)
