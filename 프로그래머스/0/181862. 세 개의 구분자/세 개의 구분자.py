def solution(myStr):
    answer = ''
    token = ['a', 'b', 'c']
    for c in myStr:
        if c in token : 
            answer+='_'
        else : 
            answer+= c 
    answer = answer.split('_')
    answer = [ans for ans in answer if ans]
    return ["EMPTY"] if len(answer) <1 else answer