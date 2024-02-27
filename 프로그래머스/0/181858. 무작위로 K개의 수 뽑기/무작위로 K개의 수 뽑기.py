def solution(arr, k):
    answer = []
    answer_set = set([])
    for v in arr : 
        if v not in answer_set : 
            answer.append(v)
            answer_set.add(v)
        if len(answer) == k : 
            break
    answer.extend([-1]*(k-len(answer)))
    return answer