import sys

n = int(sys.stdin.readline())


def fibo1(n):
    fibo = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            fibo[i] = 1
        else:
            fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[n]


def fibo2(n):
    fibo = [0 for _ in range(n + 1)]
    fibo[0] = 1
    fibo[1] = 1
    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + 1
    return fibo[n]


print(fibo1(n), fibo2(n))
