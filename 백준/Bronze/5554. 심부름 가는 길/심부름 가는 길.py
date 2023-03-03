import sys 

ans = 0
for _ in range(4):
    ans+=int(sys.stdin.readline())

print(ans//60)
print(ans%60)