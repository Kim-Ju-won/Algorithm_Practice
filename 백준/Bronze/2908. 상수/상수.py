import sys 

a, b = sys.stdin.readline().rstrip().split()
ans = a[::-1] if a[::-1] > b[::-1] else b[::-1]

print(ans)