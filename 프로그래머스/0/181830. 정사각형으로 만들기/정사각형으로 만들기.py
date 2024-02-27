def solution(arr):
    n = max(len(arr), len(arr[0]))
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            answer[i][j] = arr[i][j]
    return answer