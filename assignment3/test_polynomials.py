from polynomials import Polynomial

#Evaluate a polynomial at 3 different points
def test_check_points():
    p = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    assert p(0) == 1
    assert p(1) == 4
    assert p(50) == 2601
    #One more, why not?
    q = Polynomial(0) #Zero-polynomial
    assert q(0) == 0
    assert q(100) == 0
    assert q(0.5) == 0
    print("test_check_points() finished successfully.")

#Adding two polynomials
def test_add_polynomials():
    p = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    q = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    answer = Polynomial([6, 5, 1, 1]) #The polynomial x**3 + x**2 + 5x + 6
    assert p+q == answer
    #Testing addition of zero-polynomial as well..
    z = Polynomial([])
    assert p+z == p
    assert z+q == q
    #Testing addition of integers..
    assert p+0 == p
    assert q+5 == Polynomial([10, 3, 0, 1])
    assert p+Polynomial(5) == Polynomial([6, 2, 1])
    print("test_add_polynomials() finished successfully.")
    
#Subtracting two polynomials
def test_sub_polynomials():
    p = Polynomial([7, 0, -4, 2]) #The polynomial 2x**3 - 4x**2 + 7
    q = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    answer = Polynomial([4, -1, -4, 2, -2]) #The polynomial -2x**4 + 2x**3 - 4x**2 - x + 4
    assert p-q == answer
    print("test_sub_polynomials() finished successfully.")
    #Testing subtraction of zero-polynomial as well..
    z = Polynomial([])
    assert p-z == p
    assert z-p == Polynomial([-7, -0, 4, -2])
    #Testing subtraction of some integers
    assert p-0 == p
    assert q-5 == Polynomial([-2, 1, 0, 0, 2])

#Test degree
def test_degree():
    a = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    b = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    c = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    d = Polynomial([1, 0, 1, 0]) #The polynomial x**2 + 1
    z = Polynomial([]) #The zero-polynomial
    assert a.degree() == 2
    assert b.degree() == 3
    assert c.degree() == 4
    assert d.degree() == 2
    assert z.degree() == -1
    print("test_degree() finished successfully.")

#ADDING SOME MORE TESTS FOR THE OTHER FUNCTIONS IN Polynomial

#Test repr
def test_repr():
    a = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    b = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    c = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    d = Polynomial([1, 0, 1, 0]) #The polynomial x**2 + 1
    z = Polynomial([]) #The zero-polynomial
    assert str(a) == "x^2 + 2x + 1"
    assert str(b) == "x^3 + 3x + 5"
    assert str(c) == "2x^4 + x + 3"
    assert str(d) == "x^2 + 1"
    assert str(z) == ""
    print("test_repr() finished sucessfully.")


#Test multiplication by an integer
def test_mul():
    a = Polynomial([1, 2, 1]) #The polynomial x**2 + 2x + 1
    b = Polynomial([5, 3, 0, 1]) #The polynomial x**3 + 3x + 5
    c = Polynomial([3, 1, 0, 0, 2]) #The polynomial 2x**4 + x + 3
    assert a*3 == Polynomial([3, 6, 3])
    assert 3*a == Polynomial([3, 6, 3]) #rmul
    assert b*0 == Polynomial()
    assert c*50 == Polynomial([150, 50, 0, 0, 100])
    assert 50*c == Polynomial([150, 50, 0, 0, 100]) #rmul
    print("test_mul() finished sucessfully.")
 


test_check_points()
test_add_polynomials()
test_sub_polynomials()
test_degree()
test_repr()
test_mul()

