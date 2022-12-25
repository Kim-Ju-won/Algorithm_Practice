def d(n):
    ans = n 
    n = str(n)
    for ele in n : 
        ans+= int(ele)
    return ans

def solve(n):
    answer = [0]*(3*n)
    for i in range(1,n+1):
        answer[d(i)]+=1
    
    for i in range(1,n+1):
        if answer[i] == 0:
            print(i)

    
solve(10000)