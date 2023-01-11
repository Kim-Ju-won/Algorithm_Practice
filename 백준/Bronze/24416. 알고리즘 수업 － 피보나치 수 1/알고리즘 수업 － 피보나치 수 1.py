import sys

n = int(sys.stdin.readline())

def fibo(n,count):
    if n ==1 or n==2 : 
        count+=1
        return count  
    else:
        return fibo(n-1,count)+fibo(n-2,count)

def fibonacci(n,count):
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
        count+=1
    return count

print(fibo(n,0), fibonacci(n,0))