'''
Question : 
문제 설명
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

제한 사항
- str은 길이 1 이상인 문자열입니다.
'''

def solution(s):
    s_dict = dict()
    for ele in s : 
        if ord(ele) in s_dict : 
            s_dict[ord(ele)] += ele
        else : 
            s_dict[ord(ele)] = ele
    keys = list(s_dict.keys())
    keys.sort(reverse=True)
    answer=''
    for key in keys : 
        answer+= s_dict[key]
    return answer