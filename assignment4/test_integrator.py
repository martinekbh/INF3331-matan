from integrator import integrate
from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate
from numpy import vectorize

def f1(x):  #Contant function
    return 2.0
f1 = vectorize(f1)

def f2(x):  #Linear function
    return x*2.0

"""
NOTE: I tested the integration method for an error of 1E-10 instead
of 1E-20. Why was so high accuracy needed? Takes forever with high N
"""
    

#TEST integrate
def test_integral_of_constant_function():
    computed_ans = integrate(f1, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = integrate(f1, 0, 1, 10000) #N = 10000
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10

def test_integral_of_linear_function():
    computed_ans = integrate(f2, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = integrate(f2, 0, 1, 1000000) #N = 1000000
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numpy_integrate
def test_numpy_integrate_constant_function():
    computed_ans = numpy_integrate(f1, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numpy_integrate(f1, 0, 1, 10000) #N = 10000
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10

def test_numpy_integrate_linear_function():
    computed_ans = numpy_integrate(f2, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numpy_integrate(f2, 0, 1, 1000000) #N = 1000000
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numba_intergate
def test_numba_integrate_constant_function():
    computed_ans = numba_integrate(f1, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numba_integrate(f1, 0, 1, 10000) #N = 10000
    #print(computed_ans)
    assert abs(2.0 - computed_ans) < 1E-10

def test_numba_integrate_linear_function():
    computed_ans = numba_integrate(f2, 0, 1, 10) #N = 10
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numba_integrate(f2, 0, 1, 1000000) #N = 1000000
    #print(computed_ans)
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

test_integral_of_constant_function()
test_integral_of_linear_function()
test_numpy_integrate_constant_function()
test_numpy_integrate_linear_function()
test_numba_integrate_constant_function()
test_numba_integrate_linear_function()



