


class Fraction:
    num = 0
    den = 0
    
    def __init__(self):
        pass
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def getNumerator(self):
        return self.num
    
    def getDenominator(self):
        return self.den
    
    def setNumerator(self, numerator):
        self.num = numerator
    
    def setDenominator(self, denominator):
        self.den = denominator
    
    
    def add(self, f2):
        """Add two fractions, and return a simplified result
            f1  a string representation of a fraction (e.g. "1/2")
            f2  a string representation of a fraction (e.g. "1/2")
            return a string representation of adding those fractions
            """
        num1, den1 = int(self.getNumerator()), int(self.getDenominator())
        num2, den2 = int(f2.getNumerator()), int(f2.getDenominator())
        result = Fraction(( num1*den2 + num2*den1 ), den1*den2 )
        return result.reduce()

    def sub(self, f2):
        num1, den1 = int(self.getNumerator()), int(self.getDenominator())
        num2, den2 = int(f2.getNumerator()), int(f2.getDenominator())
        result = Fraction(( num1*den2 - num2*den1 ), den1*den2)
        return result.reduce()

    def mult(self, f2):
        num1, den1 = int(self.getNumerator()), int(self.getDenominator())
        num2, den2 = int(f2.getNumerator()), int(f2.getDenominator())
        result = Fraction(num1*num2, den1*den2)
        return result.reduce()

    def div(self, f2):
        num1, den1 = int(self.getNumerator()), int(self.getDenominator())
        den2, num2 = int(f2.getNumerator()), int(f2.getDenominator())
        result = Fraction(num1*num2, den1*den2)
        return result.reduce()

    def reduce(self):
        num, den = int(self.getNumerator()), int(self.getDenominator())
        common = Fraction.__gcd__(num,den)
        return Fraction(int(num/common), int(den/common))

    def __gcd__(a, b):
        """Calculate the Greatest Common Divisor of a and b.

            Unless b==0, the result will have the same sign as b (so that when
            b is divided by it, the result comes out positive).
            https://codereview.stackexchange.com/questions/66450/simplify-a-fraction
            """
        while b:
            a, b = b, a % b
        return a
    
    def toString(self):
        return str(self.getNumerator()) + "/" + str(self.getDenominator()) 


if (__name__) == "__main__":
    result = 0

    in1 = input("Insert first fraction here,  ")
    in2 = input("Insert second fraction here,  ")
    oper = input("Which operator do you want [+-/*]?  ")

    num1 = Fraction(in1.split("/")[0],in1.split("/")[1])
    num2 = Fraction(in2.split("/")[0],in2.split("/")[1])

    if (oper == '+'):
        result = num1.add(num2)
    elif (oper == '-'):
        result = num1.sub(num2)
    elif (oper == '*'):
        result = num1.mult(num2)
    elif (oper == '/'):
        result = num1.div(num2)
    else:
        raise ValueError("Unsupported operator.")

    print( "Result = %s" % result.toString() )

    
print("imported Fraction")