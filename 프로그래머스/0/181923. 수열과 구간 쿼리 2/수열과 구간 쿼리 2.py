def solution(arr, queries):
    answer = []
    for q in queries : 
        s, e, k = q
        ele = 10000001
        for i in range(s,e+1):
            if arr[i] > k and ele > arr[i]:
                ele = arr[i]
        if ele == 10000001:
            ele = -1
        answer.append(ele)
    return answer