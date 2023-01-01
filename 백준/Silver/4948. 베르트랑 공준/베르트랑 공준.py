import sys

def solution(n):
    if n == 1: 
        return False 
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 : 
            return False
    return True

prime_num = [0]*(123456*2+1)
for i in range(2,len(prime_num)):
    if solution(i): 
        prime_num[i] = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0 : 
        break
    count = prime_num[n+1:2*n+1].count(1)
    print(count)