'''
Question : 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(quiz):
    answer = []
    for q in quiz : 
        q = q.split()
        if q[1] == '+':
            if int(q[0])+int(q[2]) == int(q[4]): 
                answer.append("O")
            else : 
                answer.append("X")
        elif q[1] == '-':
            if int(q[0])-int(q[2]) == int(q[4]):
                answer.append("O")
            else : 
                answer.append("X")
    return answer