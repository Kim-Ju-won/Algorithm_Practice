def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i = str(i)
        check = True
        for c in i : 
            if c != '5' and c != '0':
                check = False 
                break
        if check : 
            answer.append(int(i))
    return answer if answer else [-1]