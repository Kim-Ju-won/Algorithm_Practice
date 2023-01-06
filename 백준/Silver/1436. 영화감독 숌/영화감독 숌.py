import sys

n = int(sys.stdin.readline())
ans = 666
count = 1
i = 666
while count < n : 
    i+=1
    if str(i).count('666') >= 1: 
        ans = i 
        count += 1
print(ans)