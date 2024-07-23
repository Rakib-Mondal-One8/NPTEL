# Euclid's Algorithm to find gcd of two numbers
def gcd(m, n):
    if (m < n):
        (m, n) = (n, m)
    if (m % n == 0):
        return n
    else:
        return gcd(n, m % n)


print(gcd(9, 3))
