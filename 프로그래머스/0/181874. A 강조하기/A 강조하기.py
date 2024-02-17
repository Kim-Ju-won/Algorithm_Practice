def solution(myString):
    answer = ''
    for c in myString : 
        if c == 'a' or c =='A':
            answer+= c.upper()
        else : 
            answer+= c.lower()
    return answer