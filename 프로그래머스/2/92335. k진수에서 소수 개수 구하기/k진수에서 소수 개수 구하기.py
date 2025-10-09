def is_prime(num):
    if num == 1 : 
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 : 
            return False
    return True

def solution(n, k):
    n_list = ""
    answer = 0
    
    while n : 
        n_list += str(n%k)
        n //= k
    
    
    n_list = n_list[::-1]
    n_list = n_list.split("0")
    
    # print(n_list)
    for ele in n_list : 
        if ele and is_prime(int(ele)):
            answer+=1
    
    return answer