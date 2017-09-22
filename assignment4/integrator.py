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



""" Plotting error (exercise 4,2)"""
# Function f(x) = x^2
def f(x):
    return float(x)**2.0

# Plot error of F(x) as N increases
error = np.zeros(500) #I use numpy for plotting, as its easier
N_values = np.linspace(1, 500, 500)
for i in range(0, 500):
    error[i] = abs(integrate(f, 0, 1, N_values[i]) - 1/3.0)

plt.plot(N_values, error)
plt.xlabel("N")
plt.ylabel("error")
plt.title("Error when integrating f(x)=x^2 for different values of N")
plt.savefig("quadratic_error.png")
#plt.show()
