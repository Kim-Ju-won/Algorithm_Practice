def solution(s):
    answer = True
    if len(s) != 4 and len(s)!=6 :
        answer = False
    for ele in s : 
        if 'a' <= ele and ele <='z' :
            answer = False
            break
        if 'A' <= ele and ele <='Z' :
            answer = False
            break
    return answer