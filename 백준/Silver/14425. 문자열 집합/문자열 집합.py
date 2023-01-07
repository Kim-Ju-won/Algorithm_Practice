import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
s = dict()
count = 0

for _ in range(n):
    key = sys.stdin.readline().rstrip()
    if key in s : 
        s[key]+=1
    else : 
        s[key] = 1

for _ in range(m):
    check = sys.stdin.readline().rstrip()
    if check in s : 
        count+=1
print(count)