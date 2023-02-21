import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
basket = [ i for i in range(n+1)]
for _ in range(m):
    i, j = tuple(map(int, sys.stdin.readline().split()))
    basket[i], basket[j] = basket[j], basket[i]

for ele in basket[1:]:
    print(ele, end = ' ')