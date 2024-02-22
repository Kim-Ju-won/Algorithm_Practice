def solution(strArr):
    answer = dict()
    for ele in strArr : 
        if len(ele) in answer : 
            answer[len(ele)] +=1
        else : 
            answer[len(ele)] = 1

    return max(answer.values())