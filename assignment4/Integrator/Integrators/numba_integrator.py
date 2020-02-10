from numba import jit
from numpy import sin, pi

def numba_integrate(f, a, b, N):
    """
    Integration method using numba. This does not accept numpy-vectorized functions...
    """
    f_jit = jit(nopython=True)(f)

    @jit("f8(f8, f8, f8)", nopython=True)
    def compute(a, b, N):
        n = (b-a)/float(N) #Interval length
        I = 0.0 # Will be value of integrated function
        m = 0 # Counter
        for i in range(1, int(N)):
            m += 1
            I += f_jit(a + i*n)*n
        I += f_jit(b)*n
        return I
    return compute(a, b, N)


def numba_midpoint_integrate(f, a, b, N):
    """
    Midpoint-integration method using numba. This does not accept numpy-vectorized functions...
    """

    f_jit = jit("f8(f8)", nopython=True)(f)

    @jit("f8(f8, f8, f8)", nopython=True)
    def compute(a, b, N):
        n = (b-a)/float(N) # Interval length
        I = 0.0 # Will be value of integrated function
        m = 0 # Counter
        for i in range(1, int(N+1)):
            m += 1
            I += f_jit(a + (i*n) - 0.5*n)*n
        return I
    return compute(a, b, N)
