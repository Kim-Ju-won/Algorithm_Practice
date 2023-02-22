import sys 

while True : 
    n = int(sys.stdin.readline())
    if n == -1 : 
        break
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 : 
            a, b = i, n//i
            divisor.append(a)
            if a != b and b != n: 
                divisor.append(b)
    divisor.sort()
    if sum(divisor) == n :
        print(f'{n} = ', end='')
        for ele in divisor[:-1] : 
            print(f'{ele} + ', end='')
        print(divisor[-1])
    else : 
        print(f'{n} is NOT perfect.')
