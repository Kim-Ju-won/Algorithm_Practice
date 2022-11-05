'''
Question : 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    temp = ''
    answer = 0
    
    for i in range(len(my_string)):
        if '0'<=my_string[i] <='9':
            if i!=0 and '0'<=my_string[i-1] <='9':
                temp += my_string[i]
            else : 
                temp = my_string[i]
            
        else : 
            if len(temp) >= 1:
                answer += int(temp)
            temp = ''
    
    if len(temp) >= 1:
        answer += int(temp)
        temp =''
    return answer