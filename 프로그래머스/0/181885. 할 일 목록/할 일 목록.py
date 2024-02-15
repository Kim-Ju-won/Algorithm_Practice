def solution(todo_list, finished):
    answer = []
    for i, finish in enumerate(finished):
        if not(finish): 
            answer.append(todo_list[i])
    return answer