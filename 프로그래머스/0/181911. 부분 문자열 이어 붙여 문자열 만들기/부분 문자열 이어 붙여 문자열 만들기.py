def solution(my_strings, parts):
    answer = ''
    for i, part in enumerate(parts) : 
        s, e = part
        answer+=my_strings[i][s:e+1]
    return answer