def solution(a, b):
    answer = str(a)+str(b) if str(a)+str(b) > str(b)+str(a) else str(b)+str(a)
    return int(answer)