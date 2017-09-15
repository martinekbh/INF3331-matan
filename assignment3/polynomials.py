class Polynomial:

    def __init__(self, coeffs=[]):
        """coeffs should be a list of numbers with 
        the i-th element being the coefficient a_i."""

        if isinstance(coeffs, list): #Save coefficients as list
            self.coeffs = coeffs

        elif isinstance(coeffs, int): #Save the given int as a single-entry list
            self.coeffs = [coeffs]

        else: #Polynomial-class initiated with something that is not a list or an integer
            raise TypeError

        #Check for trailing zeros in list, and remove them
        if len(self.coeffs) > 0:
            extrazero = self.coeffs[-1]
            while extrazero == 0:
                self.coeffs.pop() #Remove trailing zeo in the list
                if len(self.coeffs) > 0:
                    extrazero = self.coeffs[-1]
                else:
                    extrazero = -1 #Stop while-loop because list is empty
        

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        return len(self.coeffs)-1 #OK because trailing zeros in the list are removed in __init__

    def coefficients(self):
        """Return the list of coefficients. 
        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""

        return self.coeffs
        

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        polyvalue = 0
        i = len(self.coeffs)-1 #Counter
        while i >= 0:
            polyvalue = polyvalue + self.coeffs[i]*(x**i)
            i-=1
        return polyvalue

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 
        If p is not an int or Polynomial, should raise ArithmeticError."""

        if isinstance(p, int): #If p is an integer
            if self.degree() > -1:
                poly = Polynomial(self.coefficients())
                poly.coeffs[0] = self.coeffs[0] + p
                return poly
            else:
                return Polynomial([p])

        elif isinstance(p, Polynomial): #If p is a Polynomial
            polycoeffs = []
            i = 0 #Counter
            while i <= min(p.degree(), self.degree()):
                polycoeffs.append(p.coeffs[i]+self.coeffs[i])
                i += 1
            if p.degree() < self.degree(): #If one has higher degree than the other, append the rest of that polynomial
                polycoeffs.extend(self.coeffs[i:])
            elif self.degree() < p.degree():
                polycoeffs.extend(p.coeffs[i:])
            return Polynomial(polycoeffs)
            
        else:
            print(p, " is neither an integer nor a Polynomial")
            raise ArithmeticError("Cannot add polynomial with object that is not an integer or a Polynomial")

        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p, int): #If p is an integer
            if self.degree() > -1:
                poly = Polynomial(self.coefficients())
                poly.coeffs[0] = self.coeffs[0] - p
                return poly
            else:
                return Polynomial([-p])

        elif isinstance(p, Polynomial): #If p is a Polynomial
            polycoeffs = []
            if p.degree() <= self.degree(): #p has lower or equal degree to self
                polycoeffs.extend(self.coefficients()) #Let new polynomial have self.coefficients
                i=0
                while i <= p.degree():
                    polycoeffs[i] = polycoeffs[i] - p.coeffs[i] #Subtract p.coeffs
                    i+=1

            else: #p has higher degree than self
                i=0
                while i <= self.degree():
                    polycoeffs.append(self.coeffs[i] - p.coeffs[i]) #Subtract p from self
                    i+=1
                while i <= p.degree():
                    polycoeffs.append(0 - p.coeffs[i]) #Subtract the rest of p
                    i+=1

            return Polynomial(polycoeffs)

        else:
            print(p, " is neither an integer nor a Polynomial")
            raise ArithmeticError("Cannot subtract object that is not an integer or a Polynomial from a Polynomial")


    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        if isinstance(c, int): #If p is an integer
            poly = []
            for n in self.coeffs:
                poly.append(n*c)
            return Polynomial(poly)

        else:
            raise ArithmeticError("Cannot multiply polynomial with a non-integer object") #c is not an int


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        if isinstance(c, int): #If c is an integer
            poly = []
            for n in self.coeffs:
                poly.append(n*c)
            return Polynomial(poly)

        else:
            raise ArithmeticError("Cannot multiply polynomial with a non-integer object") #c is not an int

    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """

        power = self.degree()
        if power > 1: #Degree is 2 or more

            #Adding first part
            if self.coeffs[power] == 1:
                poly = "x^" + str(power)
            else:
                poly = str(self.coeffs[power]) + "x^" + str(power)

            #Adding middle parts
            power -= 1
            while power > 1:
                if self.coeffs[power] == 1:
                    poly = poly + " + " + "x^" + str(power)
                    power -= 1
                elif self.coeffs[power] != 0:
                    poly = poly + " + " + str(self.coeffs[power]) + "x^" + str(power)
                    power -= 1
                else: #The coefficient is zero, so do nothing
                    power -= 1

            #Adding last part - power is now 1
            if self.coeffs[power] == 1:
                poly = poly + " + x"
            elif self.coeffs[power] != 0: 
                poly = poly + " + " + str(self.coeffs[1]) + "x"
            if self.coeffs[0] != 0:
                poly = poly + " + " + str(self.coeffs[0])
            return poly



        elif power == 1:
            if self.coefiicients[power] == 1:
                poly = "x"
            else: 
                poly = str(self.coeffs[1]) + "x"
            if self.coeffs[0] != 0:
                poly = poly + " + " + str(self.coeffs[0])
            return poly

        else:
            if power == 0: #Polynomial is just a number
                return str(self.coeffs[0])
            else:
                return "" #Zero-polynomial.. unsure if best to return empty string or just "0"


    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""
        if p.degree() == self.degree(): #They must have the same degree
            #I wrote this method before i implemented the removal of trailing zeros in the __init__ method.
            #I will let it be like it is, however, as 1) it doesn't matter and 2) it shows what i did before having automatic removal of trailing zeros.
            if len(p.coeffs) <= len(self.coeffs): #self.coeffs has zeros at the end, or they have same length
                i = 0
                while i < len(p.coeffs):
                    if p.coeffs[i] != self.coeffs[i]:
                        return False #Found inequality
                    i += 1
            elif len(self.coeffs) < len(p.coeffs): #p.coeffs has zeros at the end
                i = 0
                while i < len(self.coeffs):
                    if p.coeffs[i] != self.coeffs[i]:
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
