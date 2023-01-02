import sys

n =int(sys.stdin.readline())
ans = []
for _ in range(n) : 
    ans.append(tuple(map(int, sys.stdin.readline().split())))
ans.sort()

for ele in ans :
    print(ele[0], ele[1])