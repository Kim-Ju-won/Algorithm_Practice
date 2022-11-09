'''
Question : 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(score):
    n = len(score)
    avg = [0] * n
    answer = [0] *n
    avg_dict = dict()
    
    for i in range(n) : 
        avg[i] = sum(score[i])/2
        if avg[i] not in avg_dict : 
            avg_dict[avg[i]] = [i] 
        else : 
            avg_dict[avg[i]].append(i)
    
    avg.sort(reverse=True)
    order = 1
    
    for i in range(n): 
        if i !=0 and avg[i-1] > avg[i]:
            order += len(avg_dict[avg[i-1]])
        for key in avg_dict[avg[i]] : 
            answer[key] = order
    return answer