'''
Question : 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(my_string, num1, num2):
    change1, change2 = my_string[num1], my_string[num2]
    answer = ''
    for i in range(len(my_string)):
        if i == num1 : 
            answer+= change2
        elif i == num2 : 
            answer+= change1
        else : 
            answer+= my_string[i]
    return answer