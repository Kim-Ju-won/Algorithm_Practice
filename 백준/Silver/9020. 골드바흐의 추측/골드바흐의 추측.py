import sys

def solution(i):
    if i == 1 : 
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0 : 
            return False
    return True
t = int(sys.stdin.readline())

prime_num = set()

for i in range(2,10001):
    if solution(i):
        prime_num.add(i)
check = list(prime_num)

for i in range(t):
    n = int(sys.stdin.readline())
    a, b = 0,0
    for i in range(2, n//2+1):
        if i in prime_num and (n-i) in prime_num: 
            if a == 0 and b == 0: 
                a, b = i, n-i
            elif abs(a-b) > abs(i-n+i):
                a, b = i, n-i
    print(a, b)