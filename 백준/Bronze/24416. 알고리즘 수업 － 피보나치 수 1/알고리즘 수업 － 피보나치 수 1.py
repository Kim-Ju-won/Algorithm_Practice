import sys

n = int(sys.stdin.readline())

def fibonacci(n,count):
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
        count+=1
    return count, f[n]
count_dp, count_re = fibonacci(n,0)
print(count_re,count_dp)