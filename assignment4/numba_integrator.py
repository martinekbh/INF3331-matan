from numba import jit
import numpy as np

@jit
def numba_integrate(f, a, b, N):
    """
    This function expects that f is a vectorized function...
    """
    intervals = np.linspace(a, b, N+1) #Divide [a, b] into N intervals
    f_values = f(intervals[1:]) #Find f values at the end of each interval
    I = f_values*((b-a)/float(N)) # time each f-value with the length on an interval
    return np.sum(I)

@jit
def numba_midpoint_integrate(f, a, b, N):
    """
    This function expects that f is a vectorized function...
    """
    intervals = np.linspace(a, b, N+1) #Divide [a, b] into N intervals
    midpoints = intervals - ((b-a)/float(N)) #Subtract half of interval length to find midpoints
    f_values = f(midpoints[1:]) #Find f values at the end of each interval
    I = f_values*((b-a)/float(N)) # time each f-value with the length on an interval
    return np.sum(I)

