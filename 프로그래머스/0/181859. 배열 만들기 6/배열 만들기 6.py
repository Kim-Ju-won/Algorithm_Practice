def solution(arr):
    stk = []
    for i, v in enumerate(arr):
        if stk :
            if stk[-1] == v : 
                stk.pop()
            else : 
                stk.append(v)
        else : 
            stk.append(v)
    return stk if stk else [-1]