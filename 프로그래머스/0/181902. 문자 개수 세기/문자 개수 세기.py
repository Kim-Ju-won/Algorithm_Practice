def solution(my_string):
    answer = []
    for i in range(ord('A'), ord('Z')+1):
        answer.append(my_string.count(chr(i)) )
    for i in range(ord('a'), ord('z')+1):
        answer.append(my_string.count(chr(i)))
    return answer