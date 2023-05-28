def lastdigit(n:int)->int:
    if n<=1: return n
    a,b = 0,1
    for _ in range(n-1):
        c = a+b
        c = c%10
        b,a = c,b
    return c


n = int(input("Enter the number: "))
print(lastdigit(n))
