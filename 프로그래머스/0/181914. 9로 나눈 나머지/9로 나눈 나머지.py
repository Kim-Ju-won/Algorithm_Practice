def solution(number):
    answer = 0
    for c in number : 
        answer += int(c)
    return answer %9