debug = False

def debugPrint(s):
    if (debug):
        print(s)

def isPrime(n):
    debugPrint("is %d a prime number..." % n)
    debugPrint("\tchecking %d" % 2)
    if (n == 2):
        return True
    if ( n % 2 == 0 ): 
        debugPrint("\t%d is NOT prime" % n)
        return False
    for i in range(3, int(n/2)+ 1, 2):
        debugPrint("\tchecking %d" % i)
        if ( (n % i) == 0):
            debugPrint("\t%d is NOT prime" % n)
            return False
    debugPrint("\t%d IS prime." % n)
    return True


if __name__ == "__main__":
#    isPrime(2)  # true
#    isPrime(3)  # true
#    isPrime(4)  # false
#    isPrime(12) # false
#    isPrime(29) # true
    for x in range(2,101):
        if (isPrime(x)):
            print("%d is prime" % x)
