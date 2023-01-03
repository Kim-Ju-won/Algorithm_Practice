def solution(numbers):
    answer = []
    count = 0
    for num in numbers: 
        if num == 0: 
            count+=1
        answer.append(str(num))
    if count == len(numbers):
        return '0'
    answer.sort(
        key=lambda x : 4*x,
        reverse=True)
    return  ''.join(answer)