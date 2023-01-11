def solution(brown, yellow):
    total = brown + yellow
    for i in range(1,total//2+1):
        if total % i == 0 :
            if yellow == (total//i - 2) * (i-2):
                w = max(total//i, i)
                h = min(total//i, i)
                return [w,h]
    return False

# 테두리 1줄- 갈색, 내부 노란색
# 노란색, 갈색 색칠된 격자수 매개변수
# 전체 행과 열 
# 가로 >= 세로