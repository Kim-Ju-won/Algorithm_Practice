def solution(arr, intervals):
    answer = []
    for interval in intervals : 
        a, b = interval
        answer+=arr[a:b+1]
    return answer