import sys

def solution(ele):
    count = 0 
    if ele == 1: 
        return False
    for i in range(2,int(ele**0.5)+1):
        if ele % i == 0 : 
            count += 1
        if count >= 1 : 
            return False
    return True

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
prime_sum = 0
prime_min = m+1
for ele in range(n,m+1): 
    if solution(ele) :
        prime_sum += ele 
        if prime_min >= ele:
            prime_min = ele 


if prime_sum != 0 : 
    print(prime_sum)
    print(prime_min)
else : 
    print(-1)