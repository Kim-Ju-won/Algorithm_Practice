'''
Question : my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''

def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    operand = ''
    for ch in my_string[1:] : 
        if ch in ['+','-'] : 
            operand=ch
        else : 
            if operand == '+':
                answer += int(ch)
            if operand == '-':
                answer-= int(ch)
    return answer