'''
Question : 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
'''

import sys

def solution(array, n):
    answer = sys.maxsize
    check = sys.maxsize
    for ele in array : 
        if abs(ele - n) < check : 
            answer = ele
            check = abs(ele - n)
        if abs(ele - n) == check :
            answer = min(ele, answer)
    return answer