import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a != 0:
        if a % b == 0:
            break
        a, b = b, a % b
    return b


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1, -1, -1):
    if i == n - 1:
        num, den = 1, arr[i]
    else:
        num = arr[i] * den + num
        num, den = den, num

k = gcd(den - num, den)

print((den - num) // k, den // k)
