class Rational(object):
    
    def __init__(self, num, deno):
        self._num = num
        self._deno = deno
        self._reduce()
        
    def __str__(self):
        return "Numerator : " + str(self._num) + "\nDenominator : " + str(self._deno)

    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(self._num, self._deno)
        self._num = self._num / divisor
        self._deno = self._deno / divisor

    def _gcd(self, a, b):
        (a, b) = (min(a, b), max(a, b))
        while b > 0:
            (a, b) = (b, a%b)
        return a

    def numerator(self):
        """Returns the numerator."""
        return self._num
  
    def denominator(self):
        """Returns the denominator."""
        return self._deno
    
    def __add__(self, other):
        newnum = self._num * other._deno + other._num * self._deno
        newdeno = self._deno * other._deno
        return Rational(newnum, newdeno)

    def __eq___(self, other):
        if self == other:
            return True
        elif (type(self) != type(other)):
            return False
        else:
            return self._num == other._num and self._deno == other._deno

    def __lt__(self, other):
        """Compares two rational numbers , self and other using <"""
        extremes = self._num * other._deno
        means = other._num * self._deno
        return extremes < means
    
    def __le__(self, other):
        """Compares two rational numbers , self and other using <="""
        extremes = self._num * other._deno
        means = other._num * self._deno
        return extremes <= means
    
    def __gt__(self, other):
        """Compares two rational numbers , self and other using >"""
        extremes = self._num * other._deno
        means = other._num * self._deno
        return extremes > means
    
    def __ge__(self, other):
        """Compares two rational numbers , self and other using >="""
        extremes = self._num * other._deno
        means = other._num * self._deno
        return extremes >= means

    def __sub__(self,other):
        """Returns the difference of the numbers."""
        newNumer = self._num * other._den - \
                   other._num * self._deno
        newDenom = self._deno * other._deno
        return Rational(newNumer, newDenom)
    def __mul__(self,other):
        """Returns the product of the numbers."""
        newNumer = self._num * other._num
        newDenom = self._deno * other._deno
        return Rational(newNumer, newDenom)

    def __truediv__(self,other):
        """Returns the result of division of the numbers."""
        newNumer = self._num * other._deno
        newDenom = self._deno * other._num
        return Rational(newNumer, newDenom)

    
