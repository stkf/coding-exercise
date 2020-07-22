import sys

def isPrime(val):
    isPrime = True
    for i in range (2, val/2+1):
        if (val % i ==0):
            isPrime = False
            break
    return isPrime

def reverseMe(val):
    return int(str(val)[::-1])

def reverseMeDigits(val):
    reverrsedVal = 0
    while (val !=0):
        r = int(val%10)
        reverrsedVal = reverrsedVal*10 + r
        val = int(val/10)
    return (reverrsedVal)

def findThem(top):
    circlularPrimes = []
    for num in range (2, top):
        if isPrime(num):
            reversedPrime  = reverseMeDigits(num)
            if isPrime(reversedPrime):
                circlularPrimes.append(num)
                #print "Circular prime " + str(num)
    #print(", ".join([str(i) for i in circlularPrimes]))
    print ("{0},".format(circlularPrimes))[1: -2]




if __name__ == '__main__':
    top = 50000
    if len(sys.argv) == 2:
        top = int(sys.argv[1])
    findThem(top)
