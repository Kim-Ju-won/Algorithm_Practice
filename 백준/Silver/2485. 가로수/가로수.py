import sys

n = int(sys.stdin.readline())

street = []
for _ in range(n):
    street.append(int(sys.stdin.readline()))

street.sort()
diff = []
for i in range(1,n):
    diff.append(street[i]-street[i-1])

a, b = max(diff), min(diff)
while b!=0 : 
    a, b = b, a%b
count = n-1
while count : 
    temp = 0
    for i in range(len(diff)):
        if diff[i] % a == 0 : 
            count-=1
        else : 
            count = n-1
            temp = i
            break

    if count != 0 : 
        a, b = max(diff[temp], a), min(diff[temp], a)
        while b!=0 : 
            a, b = b, a%b

ans = 0 
for ele in diff : 
    ans+=(ele//a-1)
print(ans)
