import sys 

def is_prime(k):
    if k >=2 : 
        for i in range(2, int(k**0.5)+1):
            if k % i == 0 :
                return False
        return True
    else : 
        return False

n = int(sys.stdin.readline())
array = []

for i in range(n):
    value = int(sys.stdin.readline())
    array.append(value)


for i in range(n):
    k = array[i]
    while is_prime(k) == False : 
        k+=1
    print(k)