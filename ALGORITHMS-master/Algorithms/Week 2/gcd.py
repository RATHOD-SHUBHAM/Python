# todo: Euclidian Algorithm

def computeGCD(x, y):
    while y: # while y is not zero or null or none
        x, y = y, x % y

    return x


a = 60
b = 48

print("The gcd of 60 and 48 is : ", end="")
print(computeGCD(a, b))
