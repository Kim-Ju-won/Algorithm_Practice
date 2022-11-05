'''
Question : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    minus = []
    plus =[]
    answer =[]
    for i in range(len(numbers)):
        if numbers[i] < 0 : 
            minus.append(numbers[i])
        else : 
            plus.append(numbers[i])
            
    if len(minus) >=2 : 
        minus.sort()
        answer.append(minus[-1]*minus[-2])
    if len(plus) >=2 : 
        plus.sort()
        answer.append(plus[-1]*plus[-2])
        
    numbers.sort()
    answer.append(numbers[-1]*numbers[-2])
    
    return max(answer)