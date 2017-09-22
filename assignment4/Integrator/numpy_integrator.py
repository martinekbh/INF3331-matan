import numpy as np

def numpy_integrate(f, a, b, N):
    """
    This function expects that f is a vectorized function...
    """
    intervals = np.linspace(a, b, N+1) #N+1 equally spaced points
    f_values = f(intervals[1:]) #Find f values at the end of each interval
    I = f_values*((b-a)/float(N)) # time each f-value with the length of an interval
    return np.sum(I)

def numpy_midpoint_integrate(f, a, b, N):
    """
    This function expects that f is a vectorized function...
    """
    intervals = np.linspace(a, b, N+1) #N+1 equally spaced points
    midpoints = intervals - ((b-a)/float(N)) #Subtract half the interval length to find midpoints
    f_values = f(midpoints[1:]) #Find f values at the midpoint of each interval
    I = f_values*((b-a)/float(N)) # time each f-value with the length of an interval
    return np.sum(I)

"""
def f(x):
    return np.sin(x)

print(numpy_midpoint_integrate(f, 0, np.pi, 1000))
"""


