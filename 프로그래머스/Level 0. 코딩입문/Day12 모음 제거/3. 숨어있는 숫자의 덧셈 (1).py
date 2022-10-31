'''
Question : 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    answer=0
    for alp in my_string: 
        if 48<=ord(alp)<=57:
            answer+=int(alp)
    return answer