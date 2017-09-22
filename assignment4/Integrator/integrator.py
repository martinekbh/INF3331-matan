import numpy as np
import matplotlib.pyplot as plt
#from scitools.std import *

def integrate(f, a, b, N):
    """
    Integration method that does not use any python modules (numpy)
    """
    n = (b-a)/float(N) #Interval length
    I = 0.0 # Will be value of integrated function
    m = 0 # Counter
    for i in range(1, int(N)):
        m += 1
        I += f(a + i*n)*n
    I += f(b)*n
    return I
    
def midpoint_integrate(f, a, b, N):
    """
    Integration method that does not use any python modules (numpy)
    """
    n = (b-a)/float(N) # Interval length
    I = 0.0 # Will be value of integrated function
    m = 0 # Counter
    for i in range(1, int(N+1)):
        m += 1
        I += f(a + (i*n) - 0.5*n)*n
    return I
