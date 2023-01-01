import sys

arr = list(map(int, sys.stdin.readline().split()))

ans = 0 
for ele in arr : 
    ans += ele**2

print(ans%10)