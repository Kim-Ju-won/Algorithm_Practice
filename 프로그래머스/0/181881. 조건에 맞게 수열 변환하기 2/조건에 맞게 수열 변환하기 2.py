def solution(arr):
    answer = 0
    arr_ = [0 for i in range(len(arr))]
    while True : 
        for i, ele in enumerate(arr) : 
            if ele  >= 50 and ele % 2 == 0 : 
                arr_[i] = ele//2 
            elif ele < 50 and ele % 2 :
                arr_[i] = ele *2 + 1
            else : 
                arr_[i] = arr[i]
        if arr == arr_ : 
            break
        arr = [ele for ele in arr_]
        answer+=1
    return answer