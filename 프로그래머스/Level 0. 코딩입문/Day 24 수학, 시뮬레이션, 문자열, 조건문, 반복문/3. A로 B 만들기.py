'''
Question : 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(before, after):
    before_dict = dict()
    after_dict = dict()
    
    for ele in before : 
        if ele in before_dict : 
            before_dict[ele] += 1
        else : 
            before_dict[ele] = 1
    
    for ele in after : 
        if ele in after_dict : 
            after_dict[ele] += 1
        else : 
            after_dict[ele] = 1
    
    return 1 if before_dict == after_dict else 0