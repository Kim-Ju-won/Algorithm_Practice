def solution(my_string, m, c):
    iterate = len(my_string)//m
    answer = ''
    for i in range(iterate):
        if m * (i+1) < len(my_string):
            answer+=my_string[i*m:(i+1)*m][c-1]
        else :
            answer+=my_string[i*m:][c-1]
    return answer