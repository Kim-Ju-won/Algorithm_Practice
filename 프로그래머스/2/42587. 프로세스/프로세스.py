from collections import deque

def solution(priorities, location):
    max_list = [ ele for ele in priorities]
    max_list.sort()
    process = deque([(value,idx) for idx, value in enumerate(priorities)])
    order = 1
    while process : 
        if process[0][0] == max_list[-1]:
            if process[0][1] == location : 
                return order
            else : 
                process.popleft()
                max_list.pop()
                order+=1
        else : 
            process.rotate(-1)
