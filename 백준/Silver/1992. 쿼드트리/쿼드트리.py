# 쿼드 트리(Quad Tree)
# 흑백 영상 압축 표현 
# 흰 점을 나타내는 0과 검은점 1
# 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다. 
# 주어진 영상 0으로 압축되어 있으면 압축 결과는 0 모두 1로만 되어 있으면 압축 결과는 1
# 만약 0과 1이 섞여 있으면 전체를 한번에 나타내지 못하고 
# - 왼쪽 위, 오른쪽위, 왼쪽 아래, 오른쪽 아래 4개의 영상 압축 4개의 영역 압축한 결과를 차례대로 괄호에 묶어서 표현
# 입력 n의 제곱수 1 <= n <= 64
# 출력 : 압축한 결과

import sys


def compress(graph, r, n, c, m):
    
    answer = "" 
    if n - r == 2 and m - c == 2 :

        answer += str(graph[r][c])
        answer += str(graph[r][c+1])
        answer += str(graph[r+1][c])
        answer += str(graph[r+1][c+1])
        answer = "("+ answer +")"
        if answer.count("0") == 4 : 
            answer = "0"
        elif answer.count("1") == 4 : 
            answer = "1"
        return answer

    elif n -r > 2 or m - c > 2 : 
        # 왼쪽 위 
        answer += compress(graph, r, (r+n)//2, c, (c+m)//2)
        # 오른쪽 위 
        answer += compress(graph, r, (r+n)//2, (c+m)//2, m)
        # 왼쪽 아래 
        answer += compress(graph, (r+n)//2, n, c, (c+m)//2)
        # 오른쪽 아래 
        answer += compress(graph, (r+n)//2, n,(c+m)//2, m)
        if answer.count("0") == len(answer) : 
            answer = "0"
        elif answer.count("1") == len(answer): 
            answer = "1"
        if answer != "0" and answer != "1" : 
            answer = "("+ answer +")"

        return answer


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = compress(graph, 0, n, 0, n)

if result is None : 
    print(graph[0][0])
else : 
    print(result)
