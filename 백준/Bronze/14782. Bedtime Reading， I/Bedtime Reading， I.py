import sys

n = int(sys.stdin.readline())
sum_divisor = set([])

for i in range(1, n // 2):
    if n % i == 0:
        sum_divisor.add(i)
        sum_divisor.add(n // i)

print(sum(sum_divisor))
