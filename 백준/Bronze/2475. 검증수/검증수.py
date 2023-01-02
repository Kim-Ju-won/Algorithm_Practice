import sys

num = list(map(int, sys.stdin.readline().split()))
ans = 0 
for ele in num : 
    ans+= ele**2

print(ans%10)
