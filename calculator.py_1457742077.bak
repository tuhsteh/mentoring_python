
def add(f1, f2):
    """Add two fractions, and return a simplified result
        f1  a string representation of a fraction (e.g. "1/2")
        f2  a string representation of a fraction (e.g. "1/2")
        return a string representation of adding those fractions
        """
    num1, den1 = int(f1.split('/')[0]), int(f1.split('/')[1])
    num2, den2 = int(f2.split('/')[0]), int(f2.split('/')[1])
    result = str( num1*den2 + num2*den1 ) + "/" + str( den1*den2 )
    return reduce(result)

def sub(f1, f2):
    num1, den1 = int(f1.split('/')[0]), int(f1.split('/')[1])
    num2, den2 = int(f2.split('/')[0]), int(f2.split('/')[1])
    result = str( num1*den2 - num2*den1 ) + "/" + str( den1*den2 )
    return reduce(result)

def mult(f1, f2):
    num1, den1 = int(f1.split('/')[0]), int(f1.split('/')[1])
    num2, den2 = int(f2.split('/')[0]), int(f2.split('/')[1])
    result = str( num1*num2 ) + "/" + str( den1*den2 )
    return reduce(result)

def div(f1, f2):
    num1, den1 = int(f1.split('/')[0]), int(f1.split('/')[1])
    den2, num2 = int(f2.split('/')[0]), int(f2.split('/')[1])
    result = str( num1*num2 ) + "/" + str( den1*den2 )
    return reduce(result)

def reduce(f1):
    num, den = int(f1.split('/')[0]), int(f1.split('/')[1])
    common = gcd(num,den)
    return str(int(num/common)) + "/" + str(int(den/common))

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        https://codereview.stackexchange.com/questions/66450/simplify-a-fraction
        """
    while b:
        a, b = b, a % b
    return a



result = 0

num1 = input("Insert first fraction here,  ")
num2 = input("Insert second fraction here,  ")
oper = input("Which operator do you want [+-/*]?  ")

if (oper == '+'):
    result = add(num1, num2)
elif (oper == '-'):
    result = sub(num1, num2)
elif (oper == '*'):
    result = mult(num1, num2)
elif (oper == '/'):
    result = div(num1, num2)
else:
    raise ValueError("Unsupported operator.")

print( "Result = %s" % result )
