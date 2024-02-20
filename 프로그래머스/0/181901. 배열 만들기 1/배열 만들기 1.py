def solution(n, k):
    answer = []
    multiple = k 
    while multiple <= n : 
        answer.append(multiple)
        multiple+=k
    return answer