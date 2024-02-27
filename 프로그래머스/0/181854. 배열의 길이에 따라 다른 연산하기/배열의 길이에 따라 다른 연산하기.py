def solution(arr, n):
    if len(arr) % 2 :
        k = 0
    else : 
        k = 1
    for i in range(k,len(arr),2):
        arr[i]+=n
    return arr
        
