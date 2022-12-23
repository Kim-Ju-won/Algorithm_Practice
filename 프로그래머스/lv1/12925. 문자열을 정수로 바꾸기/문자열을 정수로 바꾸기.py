def solution(s):
    if s[0] == '-': 
        answer = int(s[1:])
        answer = -answer
    else : 
        answer = int(s)
    return answer