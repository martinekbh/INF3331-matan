from polynomials import Polynomial

#Evaluate a polynomial at 3 different points
def test_check_points():
    p = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    assert p(0) == 1
    assert p(1) == 4
    assert p(50) == 2601

#Adding two polynomials
def test_add_polynomials():
    p = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    q = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    answer = Polynomials([6, 5, 1, 1]) #The polynomial x**3 + x**2 + 5x + 6
    assert p+q == answer
    
#Subtracting two polynomials
def test_sub_polynomials():
    p = Polynomial([7, 0, -4, 2]) #The polynomial 2x**3 - 4x**2 + 7
    q = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    answer = Polynomial([4, -1, -4, 2, -2]) #The polynomial -2x**4 + 2x**3 - 4x**2 - x + 4
    assert p-q == answer

#Test degree
def test_degree():
    a = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    b = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    c = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    d = Polynomials([1, 0, 1, 0]) #The polynomial x**2 + 1
    assert a.degree() == 2
    assert b.degree() == 3
    assert c.degree() == 3
    assert d.degree() == 2
 
test_check_points()
test_add_polynomials()
test_sub_polynomials()
test_degree()
