import time
import numpy as np
from integrator import integrate
from numpy_integrator import numpy_integrate
from numba_integrator import numba_integrate
import matplotlib.pyplot as plt

def f1(x):
    return x**3.0

def f2(x):
    return np.exp(x)


"""TEST INTEGRATION TIME OF f1"""
integr = []
numpy_integr = []
numba_integr = []

#Test for N=10**5
start_time = time.time()
F1 = integrate(f1, 0, 1, 1000000)
runtime = time.time() - start_time
integr.append(runtime)
print("integrate() took %s seconds to integrate x^3 from 0 to 1 with N=1000000" % (runtime))
start_time = time.time()
F1 = numpy_integrate(f1, 0, 1, 1000000)
runtime = time.time() - start_time
numpy_integr.append(runtime)
print("numpy_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=1000000" % (runtime))
start_time = time.time()
F1 = numba_integrate(f1, 0, 1, 1000000)
runtime = time.time() - start_time
numba_integr.append(runtime)
print("numba_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=1000000" % (runtime))

#Test for N=10**6
start_time = time.time()
F1 = integrate(f1, 0, 1, 10000000)
runtime = time.time() - start_time
integr.append(runtime)
print("integrate() took %s seconds to integrate x^3 from 0 to 1 with N=10000000" % (runtime))
start_time = time.time()
F1 = numpy_integrate(f1, 0, 1, 10000000)
runtime = time.time() - start_time
numpy_integr.append(runtime)
print("numpy_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=10000000" % (runtime))
start_time = time.time()
F1 = numba_integrate(f1, 0, 1, 10000000)
runtime = time.time() - start_time
numba_integr.append(runtime)
print("numba_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=10000000" % (runtime))

#Test for N=10**7
start_time = time.time()
F1 = integrate(f1, 0, 1, 100000000)
runtime = time.time() - start_time
integr.append(runtime)
print("integrate() took %s seconds to integrate x^3 from 0 to 1 with N=100000000" % (runtime))
start_time = time.time()
F1 = numpy_integrate(f1, 0, 1, 100000000)
runtime = time.time() - start_time
numpy_integr.append(runtime)
print("numpy_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=100000000" % (runtime))
start_time = time.time()
F1 = numba_integrate(f1, 0, 1, 100000000)
runtime = time.time() - start_time
numba_integr.append(runtime)
print("numba_integrate() took %s seconds to integrate x^3 from 0 to 1 with N=100000000" % (runtime))

N_values = [6, 7, 8]
plt.gcf().clear() #Clear any previous plots
plt.plot(N_values, integr, "go")
plt.plot(N_values, numpy_integr, "ro")
plt.plot(N_values, numba_integr, "bo")
plt.plot(N_values, integr, "-g")
plt.plot(N_values, numpy_integr, "-r")
plt.plot(N_values, numba_integr, "-b")
plt.xlim([6, 8])
plt.legend(["integrate", "numpy_integrate", "numba_integrate"])
plt.xlabel("N value: 10^n")
plt.ylabel("runtime in seconds")
plt.title("Runtime of different integration methods when integrating x^3 with different N values")
plt.savefig("Runtime_integration_methods.png")
plt.show()



"""TEST INTEGRATION TIME OF f2"""
#Test for N=10**5
start_time = time.time()
F1 = integrate(f2, 0, 1, 100000)
print("integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=100000" % (time.time() - start_time))
start_time = time.time()
F1 = numpy_integrate(f2, 0, 1, 100000)
print("numpy_integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=100000" % (time.time() - start_time))
#Test for N=10**6
start_time = time.time()
F1 = integrate(f2, 0, 1, 1000000)
print("integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=1000000" % (time.time() - start_time))
start_time = time.time()
F1 = numpy_integrate(f2, 0, 1, 1000000)
print("numpy_integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=1000000" % (time.time() - start_time))
#Test for N=10**7
start_time = time.time()
F1 = integrate(f2, 0, 1, 10000000)
print("integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=10000000" % (time.time() - start_time))
start_time = time.time()
F1 = numpy_integrate(f2, 0, 1, 10000000)
print("numpy_integrate() took %s seconds to integrate exp(x) from 0 to 1 with N=10000000" % (time.time() - start_time))


