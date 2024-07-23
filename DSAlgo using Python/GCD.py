# Using Lists
def gcd(a, b):
    fn = []
    for i in range(1, a + 1):
        if (a % i) == 0:
            fn.append(i)
    fm = []
    for i in range(1, b + 1):
        if (b % i) == 0:
            fm.append(i)
    cd = []
    for d in fn:
        if d in fm:
            cd.append(d)
    return cd[-1]


# No lists and optimized algo
def gcd_optimized(m, n):
    i = min(m, n)
    while i > 0:
        if (m % i == 0) and (n % i == 0):
            return i
        else:
            i -= 1


a = int(input())
b = int(input())
print(gcd_optimized(a, b))
