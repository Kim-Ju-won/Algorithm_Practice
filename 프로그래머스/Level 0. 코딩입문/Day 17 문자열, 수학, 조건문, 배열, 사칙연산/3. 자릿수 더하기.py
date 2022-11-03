'''
Question : 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
'''

def solution(n):
    n = str(n)
    answer = 0
    for ele in n : 
        answer += int(ele)
    return answer