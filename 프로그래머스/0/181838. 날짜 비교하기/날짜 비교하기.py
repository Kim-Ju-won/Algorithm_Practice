def solution(date1, date2):
    answer = 0
    a=int(str(date1[0])+str(date1[1])+str(date1[2]))
    b=int(str(date2[0])+str(date2[1])+str(date2[2]))
    if a<b:
        answer+=1
    else:
        answer+=0
    return answer