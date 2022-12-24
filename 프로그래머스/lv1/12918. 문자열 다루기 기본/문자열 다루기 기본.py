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

'''
다른 풀이 : 
return s.isdigit() and len(s) in (4, 6)
'''