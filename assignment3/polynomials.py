class Polynomial:

    def __init__(self, coefficients=[]):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""

        self.coefficients = coefficients
        

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        i = len(self.coefficients)-1
        while i >= 0:
            if self.coefficients[i] != 0:
                return i
            i -= 1
        return -1 #Zero-polynomial


    def coefficients(self):
        """Return the list of coefficients. 

        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""
        
        raise NotImplemented

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        polyvalue = 0
        i = len(self.coefficients)-1 #Counter
        while i >= 0:
            polyvalue = polyvalue + self.coefficients[i]*(x**i)
            i-=1
        return polyvalue

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 
        If p is not an int or Polynomial, should raise ArithmeticError."""

        if isinstance(p, int): #If p is an integer
            #print(p, " is an integer\n")
            if self.degree() > -1:
                poly = Polynomial(self.coefficients)
                poly.coefficients[0] = self.coefficients[0] + p
                #print("p1: ", self.coefficients, ", p: ", p, ", p1+p2: ", poly.coefficients)
                return poly
            else:
                #print("p1: ", self.coefficients, ", p: ", p, ", p1+p2: ", poly.coefficients)
                return Polynomial([p])

        elif isinstance(p, Polynomial): #If p is a Polynomial
            #print(p.coefficients, " is a Polynomial\n")
            polycoeffs = []
            i = 0 #Counter
            while i <= min(p.degree(), self.degree()):
                polycoeffs.append(p.coefficients[i]+self.coefficients[i])
                i += 1
            if p.degree() < self.degree(): #If one has higher degree than the other, append the rest of that polynomial
                polycoeffs.extend(self.coefficients[i:])
            elif self.degree() < p.degree():
                polycoeffs.extend(p.coefficients[i:])
            #print("p1: ", self.coefficients, ", p2: ", p.coefficients, ", p1+p2: ", polycoeffs)
            return Polynomial(polycoeffs)
            
        else:
            print(p, " is neither an integer nor a Polynomial")
            raise ArithmeticError

        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p, int): #If p is an integer
            #print(p, " is an integer\n")
            if self.degree() > -1:
                poly = Polynomial(self.coefficients)
                poly.coefficients[0] = self.coefficients[0] - p
                #print("p1: ", self.coefficients, ", p: ", p, ", p1+p2: ", poly.coefficients)
                return poly
            else:
                #print("p1: ", self.coefficients, ", p: ", p, ", p1+p2: ", poly.coefficients)
                return Polynomial([-p])

        elif isinstance(p, Polynomial): #If p is a Polynomial
            #print(p.coefficients, " is a Polynomial\n")
            polycoeffs = []
            if p.degree() <= self.degree(): #p has lower or equal degree to self
                polycoeffs.extend(self.coefficients) #Let new polynomial have self.coefficients
                i=0
                while i <= p.degree():
                    polycoeffs[i] = polycoeffs[i] - p.coefficients[i] #Subtract p.coefficients
                    i+=1
                #print("p1: ", self.coefficients, ", p2: ", p.coefficients, ", p1-p2: ", polycoeffs)

            else: #p has higher degree than self
                i=0
                while i <= self.degree():
                    polycoeffs.append(self.coefficients[i] - p.coefficients[i]) #Subtract p from self
                    i+=1
                while i <= p.degree():
                    polycoeffs.append(0 - p.coefficients[i]) #Subtract the rest of p
                    i+=1
                #print("p1: ", self.coefficients, ", p2: ", p.coefficients, ", p1-p2: ", polycoeffs)

            return Polynomial(polycoeffs)

        else:
            print(p, " is neither an integer nor a Polynomial")
            raise ArithmeticError

 


    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        if isinstance(p, int): #If p is an integer
            pcoefficients = []
            for n in self.coefficients:
                pcoefficients.append(n*p)
            return Polynomial(pcoefficients)

        else:
            raise ArithmeticError #p is not an int


        raise NotImplemented


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        raise NotImplemented
    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        raise NotImplemented

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""
        if p.degree() == self.degree(): #They must have the same degree
            if len(p.coefficients) <= len(self.coefficients): #self.coefficients has zeros at the end, or they have same length
                i = 0
                while i < len(p.coefficients):
                    if p.coefficients[i] != self.coefficients[i]:
                        return False #Found inequality
                    i += 1
            elif len(self.coefficients) < len(p.coefficients): #p.coefficients has zeros at the end
                i = 0
                while i < len(self.coefficients):
                    if p.coefficients[i] != self.coefficients[i]:
                        return False #Found inequality
                    i += 1
            return True #If function has not returned false yet, the polynomials are equal
        else:
            return False #Polynomials of different degrees are not equal


def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))

    
    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
