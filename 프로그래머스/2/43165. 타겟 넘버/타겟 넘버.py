import sys
sys.setrecursionlimit(10**9)
answer = 0

def dfs(s,numbers,target, temp):
    global answer
    if s == len(numbers)-1 : 
        if target == temp+numbers[s]:
            answer+=1
        else : 
            if target == temp-numbers[s]:
                answer+=1
    else : 
        dfs(s+1, numbers, target, temp+numbers[s])
        dfs(s+1, numbers, target, temp-numbers[s])
        
def solution(numbers, target):
    s = 0
    temp = 0
    dfs(s, numbers, target, temp)
    return answer