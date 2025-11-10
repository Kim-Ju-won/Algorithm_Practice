import sys
from collections import deque

n = int(sys.stdin.readline())

problems = [ sys.stdin.readline().rstrip() for _ in range(n)]
score = 0 
problem_list = deque([])

for i in range(n):
    checking = False
    
    problem = problems[i].split()
    if len(problem) == 3 : 
        point, minute = int(problem[1]), int(problem[2]) - 1 # 새로운 문제를 받고 문제를 품
        checking = True

    if checking : 
        if minute == 0 : 
            score += point
        else : 
            problem_list.appendleft([point, minute])
    else : 
        if len(problem_list) > 0 : 
            point, minute = problem_list[0]
            if minute - 1 == 0 : 
                score += point 
                problem_list.popleft()
            else : 
                problem_list[0][1] -= 1

print(score)