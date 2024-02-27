def solution(num_str):
    answer = 0
    for i, v in enumerate(num_str) : 
        answer+=int(v)
    return answer