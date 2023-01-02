import sys

n =int(sys.stdin.readline())
ans = []
for _ in range(n) : 
    x, y = tuple(map(int, sys.stdin.readline().split()))
    ans.append((y,x))
ans.sort()

for ele in ans :
    print(ele[1], ele[0])