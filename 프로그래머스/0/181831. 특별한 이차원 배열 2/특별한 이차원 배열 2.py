def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i] :
                return 0
    return 1