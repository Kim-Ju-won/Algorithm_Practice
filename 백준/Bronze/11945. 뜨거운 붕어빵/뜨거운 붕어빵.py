import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
ans = []
for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    temp.reverse()
    ans.append(''.join(temp))

for ele in ans : 
    print(ele)