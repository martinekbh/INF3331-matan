from integrator import integrate, midpoint_integrate
from numpy_integrator import numpy_integrate, numpy_midpoint_integrate
from numba_integrator import numba_integrate, numba_midpoint_integrate
from numpy import vectorize

def f(x):  #Constant function
    return 2.0

def f2(x):  #Linear function
    return x*2.0
    

#TEST integrate
def test_integral_of_constant_function():
    print("yay")
    f1 = vectorize(f)
    computed_ans = integrate(f1, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = integrate(f1, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_integral_of_linear_function():
    computed_ans = integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numpy_integrate
def test_numpy_integrate_constant_function():
    f1 = vectorize(f)
    computed_ans = numpy_integrate(f1, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numpy_integrate(f1, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_numpy_integrate_linear_function():
    computed_ans = numpy_integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numpy_integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numba_intergate
def test_numba_integrate_constant_function():
    computed_ans = numba_integrate(f, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numba_integrate(f, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_numba_integrate_linear_function():
    computed_ans = numba_integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numba_integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)


#TEST midpoint_integrate
def test_midpoint_integral_of_constant_function():
    f1 = vectorize(f)
    computed_ans = midpoint_integrate(f1, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = midpoint_integrate(f1, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_midpoint_integral_of_linear_function():
    computed_ans = midpoint_integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = midpoint_integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numpy_integrate
def test_numpy_midpoint_integrate_constant_function():
    f1 = vectorize(f)
    computed_ans = numpy_midpoint_integrate(f1, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numpy_midpoint_integrate(f1, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_numpy_midpoint_integrate_linear_function():
    computed_ans = numpy_midpoint_integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numpy_midpoint_integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

#TEST numba_integrate
def test_numba_midpoint_integrate_constant_function():
    computed_ans = numba_midpoint_integrate(f, 0, 1, 10) #N = 10
    assert abs(2.0 - computed_ans) < 1E-10
    computed_ans = numba_midpoint_integrate(f, 0, 1, 10000) #N = 10000
    assert abs(2.0 - computed_ans) < 1E-10

def test_numba_midpoint_integrate_linear_function():
    computed_ans = numba_midpoint_integrate(f2, 0, 1, 10) #N = 10
    assert abs(1.0 - computed_ans) < (1.0/10 + 1E-10)
    computed_ans = numba_midpoint_integrate(f2, 0, 1, 1000000) #N = 1000000
    assert abs(1.0 - computed_ans) < (1.0/1000000 + 1E-10)

