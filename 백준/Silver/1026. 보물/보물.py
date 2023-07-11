import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()
ans = 0
for i in range(n):
    ans += a[i] * b[i]
print(ans)