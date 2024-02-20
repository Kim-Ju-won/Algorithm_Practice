def solution(arr):
    answer = []
    if 2 in arr : 
        for i, v in enumerate(arr):
            if v == 2: 
                answer.append(i)
        return arr[answer[0]:answer[-1]+1]
    else : 
        return [-1]