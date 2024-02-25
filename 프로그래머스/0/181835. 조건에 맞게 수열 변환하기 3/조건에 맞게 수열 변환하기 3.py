def solution(arr, k):
    answer = []
    return [ele*k for ele in arr] if k % 2 else [ele+k for ele in arr]