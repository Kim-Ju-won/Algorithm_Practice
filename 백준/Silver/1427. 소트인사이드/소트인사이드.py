import sys

n =sys.stdin.readline().rstrip()
ans = []
for c in n : 
    ans.append(c)
ans.sort(reverse=True)
print(''.join(ans))