def solution(alp, cop, problems):
    max_alp = max([x[0] for x in problems])
    max_cop = max([x[1] for x in problems])
    problems.sort(key = lambda x:(x[0], x[1], -x[2]/x[4], x[3]/x[4], x[4]))
    problems_dict = dict()
    for problem in problems : 
        alp_req, cop_req, alp_rwd, cop_rwd, cost  = problem 
        problems_dict[(alp_req, cop_req)] = (alp_rwd, cop_rwd, cost)
    
    answer = (max_alp - alp)+(max_cop-cop)
    
    DP = [[ 0 for _ in range(max_cop+1)] for _ in  range(max_alp+1)]
    
    for i in range(alp+1, max_alp):
        DP[i][cop] = DP[i-1][cop] + 1
    
    for i in range(cop+1, max_cop):
        DP[alp][i] = DP[alp][i-1] + 1
        
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            DP[i][j] = (i-alp)+(j-cop)
        
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            print(DP[i][j], end = " ")
        print()
    

    return answer