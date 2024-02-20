def solution(numbers, n):
    s = 0
    for i, number in enumerate(numbers):
        s+=number
        if s > n: 
            return s 