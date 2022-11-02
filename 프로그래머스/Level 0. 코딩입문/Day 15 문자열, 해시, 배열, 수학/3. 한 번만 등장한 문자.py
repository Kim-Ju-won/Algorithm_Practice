'''
Question : 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
'''

def solution(s):
    answer_dict = dict()
    answer = []
    
    for alp in s : 
        if alp not in answer_dict : 
            answer_dict[alp]=1  
        else : 
            answer_dict[alp]+=1 
    
    for key in answer_dict.keys() : 
        if answer_dict[key] == 1: 
            answer.append(key)
    answer.sort()
    
    return ''.join(answer)