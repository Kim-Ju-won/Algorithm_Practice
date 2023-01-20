import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()
prime = set()
min_arr = arr[0]
gcd_list = []
for i in range(n):
    arr[i]-=min_arr

if len(arr) > 2 : 
    gcd = arr[1]
    a = arr[2]
else : 
    gcd = arr[1]
    a = arr[1]

while a % gcd != 0 : 
    a, gcd = gcd, a%gcd

if gcd > 1 : 
    gcd_list.append(gcd)
    for j in range(2, int(gcd**0.5)+1):
        if gcd % j == 0 : 
            gcd_list.append(j)
            gcd_list.append(gcd //j )

for gcd in gcd_list : 
    check = True
    for i in range(1,n):
        if arr[i] % gcd != 0 : 
            check = False 
            break
    if check: 
        prime.add(gcd)
    
for i in range(n):
    arr[i]+=1

prime = list(prime)
prime.sort()

for ele in prime : 
    print(ele, end = ' ')
