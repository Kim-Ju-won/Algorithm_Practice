import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
basket = [ i for i in range(n+1)]
for _ in range(m):
    i, j = tuple(map(int, sys.stdin.readline().split()))
    count = (j-i)//2
    for index in range((j-i)//2+1):
        basket[i+index], basket[j-index] = basket[j-index], basket[i+index],
for ele in basket[1:]:
    print(ele, end = ' ')