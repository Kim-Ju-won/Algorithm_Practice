'''
Question : 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
'''
def solution(array):
    array_dict = dict()
    for ele in array : 
        if ele in array_dict : 
            array_dict[ele] += 1
        else : 
            array_dict[ele] = 1
    max_list = [-1]
    max_num = 0
    for ele in array_dict.keys() : 
        if array_dict[ele] > max_num:
            max_list = [ele]
            max_num = array_dict[ele]
        elif array_dict[ele] == max_num:
            max_list.append(array_dict[ele])
            
    if len(max_list) >=2:
        answer = -1
    else : 
        answer =  max_list[-1]
    
    return answer