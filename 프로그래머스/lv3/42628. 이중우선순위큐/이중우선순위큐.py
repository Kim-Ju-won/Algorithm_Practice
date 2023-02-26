import heapq

def solution(operations):
    answer = []
    for op in operations :
        op, num = op.split()
        if op == 'I':
            heapq.heappush(answer, int(num))
        elif op == 'D':
            if answer : 
                if num == '1':
                    answer.sort()
                    answer.pop()
                elif num == '-1':
                    heapq.heappop(answer)
    if answer : 
        answer.sort()
        return [answer[-1], answer[0]]
    else : 
        return [0,0]