'''
Question : 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
'''

def solution(bin1, bin2):
    
    num1 = 0
    num2 = 0
    result = 0 
    
    for i in range(len(bin1)-1,-1,-1):
        if bin1[i] == '1':
            num1+=2**(len(bin1)-i-1)
    
    for i in range(len(bin2)-1,-1,-1):
        if bin2[i]=='1':
            num2+=2**(len(bin2)-i-1)
    
    result = num1+num2
    answer =[]
    
    while result >=0 : 
        answer.append(str(result%2))
        result //=2
        if result == 0: 
            break
    answer.reverse()
    return ''.join(answer)