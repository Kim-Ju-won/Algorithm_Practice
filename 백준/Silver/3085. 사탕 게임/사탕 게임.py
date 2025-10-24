import sys
from collections import deque


def in_range(x, y, n):
    return True if 0 <= x < n and 0 <= y < n else False

n = int(sys.stdin.readline())
arr = [ list(sys.stdin.readline()) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

changed = [[False for _ in range(n)] for _ in range(n)]
answer = 0 

for i in range(n):
    for j in range(n):
        count = 0 
        for x, y in zip(dx, dy):
            if in_range(i+x, j+y, n) and arr[i+x][j+y] != arr[i][j] and changed[i+x][j+y] is False:
                max_count = 0 
                arr[i+x][j+y], arr[i][j] = arr[i][j], arr[i+x][j+y]
                visited = [[False for _ in range(n)] for _ in range(n)]
                for r in range(n):
                    count = 1
                    for c in range(1,n):

                        if arr[r][c-1] == arr[r][c]: 
                            count +=1
                            max_count = max(max_count, count)
                        else : 
                            max_count = max(max_count, count)
                            count = 1

                for r in range(n):
                    count = 1
                    for c in range(1, n):
                        if arr[c][r] == arr[c-1][r]: 
                            count +=1
                            max_count = max(max_count, count)
                        else : 
                            max_count = max(max_count, count)
                            count = 1

                arr[i+x][j+y], arr[i][j] = arr[i][j], arr[i+x][j+y]
                answer = max(max_count, answer)
        if  count > 0 : 
            changed[i][j] = True
                
print(answer)