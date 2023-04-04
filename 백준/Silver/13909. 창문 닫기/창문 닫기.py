import sys

n = int(sys.stdin.readline())

ans = 1
while (ans+1) * (ans+1)  <= n : 
    ans+=1 

print(ans)