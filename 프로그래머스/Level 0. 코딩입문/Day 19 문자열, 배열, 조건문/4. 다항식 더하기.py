'''
Question : 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
'''

def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x_rank = 0
    num = 0
    
    for ele in polynomial : 
        if ele[-1] =='x':
            if len(ele) == 1 : 
                x_rank +=1
            else : 
                x_rank += int(ele[:-1])
        else : 
            num+= int(ele)
            
    if x_rank != 0 and num == 0 :
        if x_rank == 1: 
            answer ='x'
        else : 
            answer = str(x_rank)+'x'
    elif x_rank == 0 and num != 0 : 
        answer = str(num)
    else : 
        if x_rank == 1: 
            answer ='x + '+str(num)
        else : 
            answer = str(x_rank)+'x + '+str(num)

    return answer