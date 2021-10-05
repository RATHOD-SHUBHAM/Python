a, b = [int(i) for i in input().split()]


def euclid_lcm(a, b):
    if b == 0:
        return a
    c = a % b
    return euclid_lcm(b, c)


if a > b:
    lcm = euclid_lcm(a, b)
else:
    lcm = euclid_lcm(b, a)

print(a * b // lcm)
