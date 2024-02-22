def solution(arr):
    n = len(arr)
    i = 1024 
    while n <= i : 
        i//=2
    i*=2
    return arr + [0] * (i-len(arr))