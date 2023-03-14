import sys 

t = int(sys.stdin.readline())

prime_list = [1]*1000001

for i in range(2,1001):
    k = 2 
    while k*i < len(prime_list):
        prime_list[k*i] = 0
        k+=1
prime_set =set()
for i in range(len(prime_list)) : 
    if prime_list[i] == 1 : 
        prime_set.add(i)

keys = list(prime_set)
keys.sort()

for _ in range(t):
    k = int(sys.stdin.readline())
    ans = 0
    for key in keys[2:] : 
        if key > k//2 : 
            break
        if (k-key) in prime_set : 
            ans+=1
    print(ans)
