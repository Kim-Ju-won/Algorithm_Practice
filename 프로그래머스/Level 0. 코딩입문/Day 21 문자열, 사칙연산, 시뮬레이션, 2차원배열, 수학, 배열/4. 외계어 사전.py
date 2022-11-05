'''
Question : PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
'''

def solution(spell, dic):
    spell_dict = dict()
    dic_dict_list = []
    
    for ele in spell : 
        if ele in spell_dict : 
            spell_dict[ele]+=1
        else : 
            spell_dict[ele]=1
            
    for ele in dic : 
        ele_dict = dict()
        for alp in ele : 
            if alp in ele_dict : 
                ele_dict[alp]+=1
            else : 
                ele_dict[alp]=1
        dic_dict_list.append(ele_dict)
    answer = 2
    
    for ele in dic_dict_list : 
        if ele == spell_dict : 
            answer =1 
            break
    return answer