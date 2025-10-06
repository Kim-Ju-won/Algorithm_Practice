def solution(n, tops):
    answer = 0
    DP_n = [0 for _ in range(n+2)]
    DP_n1 = [0 for _ in range(n+2)]
    tops = [0] + tops
    for i in range(n+2):
        if i == 1 : 
            if tops[i] == 1 :
                DP_n[i] = 3
            else : 
                DP_n[i] = 2
            DP_n1[i] = 1
        elif i == 2:
            if i <= n and tops[i] == 1 :
                DP_n[i] = (DP_n[i-1] * 3 + 2)%10007
            elif i > n or (tops[i] == 0): 
                DP_n[i] = (DP_n[i-1] * 2 + 1)%10007
                
            if tops[i-1] == 1 : 
                DP_n1[i] = (DP_n[i-1] + DP_n1[i-1] )
            elif (tops[i-1] == 0): 
                DP_n1[i] = (DP_n1[i-1] * 2 + 1)%10007
                
        elif i >= 2 :   
            if i <= n and tops[i] == 1 :
                DP_n[i] = (DP_n[i-1] * 3 + DP_n1[i-1] * 2)%10007
            elif i > n or (tops[i] == 0): 
                DP_n[i] = (DP_n[i-1] * 2 + DP_n1[i-1])%10007
                
            if tops[i-1] == 1:
                DP_n1[i] = (DP_n[i-1] + DP_n1[i-1])%10007
            elif (tops[i-1] == 0): 
                DP_n1[i] = (DP_n1[i-1] * 2 + DP_n[i-2])%10007
            
            
    return (DP_n1[-1])