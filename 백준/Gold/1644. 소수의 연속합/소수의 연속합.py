import sys 


n = int(sys.stdin.readline())
prime_candidate = [ 0 for _ in range(n+1)]
prime_numbers =[]
check = 2
while True : 
    if check**2 > n : 
        break 
    if prime_candidate[check] == 0 :
        i = 2 
        bound = check*i 
        while bound <= n : 
            prime_candidate[bound] = 1
            i+=1
            bound = check*i
    check+=1

for i in range(2,n+1):
    if prime_candidate[i] == 0 : 
        prime_numbers.append(i)

ans = 0 

if prime_numbers : 
    j = 1
    sum_prime = prime_numbers[0]

    for i in range(len(prime_numbers)):
        while j < len(prime_numbers) and sum_prime < n : 
            sum_prime+=prime_numbers[j]
            j+=1
        if sum_prime == n : 
            ans+=1
        sum_prime-=prime_numbers[i]

print(ans)