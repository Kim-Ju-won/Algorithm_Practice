import sys

n =int(sys.stdin.readline())
ans = []
for _ in range(n) : 
    ans.append(sys.stdin.readline().rstrip())
ans.sort(key=lambda x : (len(x),x))

for i in range(n) :
    if i==0 : 
        print(ans[i])
    else: 
        if ans[i] != ans[i-1]:
            print(ans[i])
    