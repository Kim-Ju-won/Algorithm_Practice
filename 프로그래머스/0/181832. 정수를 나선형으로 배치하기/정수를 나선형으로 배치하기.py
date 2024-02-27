def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    k, i, j = 1, 0, 0
    direction = "right"
    while k <= n * n:
        if answer[i][j] == 0:
            answer[i][j] = k
            k+=1
        else:
            if direction == "right" :
                if j + 1 == n :
                    direction = "down"
                elif answer[i][j + 1] != 0:
                    direction = "down"
                else : 
                    j+=1
            elif direction == "down" :
                if i + 1 == n :
                    direction = "left"
                elif answer[i+1][j] != 0:
                    direction = "left"
                else : 
                    i += 1
 
            elif direction =="left":
                if j - 1 == -1 :
                    direction = "up"
                elif answer[i][j-1]!= 0:
                    direction = "up"
                else : 
                    j -= 1
            elif direction == "up":
                if i - 1 == -1 : 
                    direction = "right"
                elif answer[i-1][j] != 0:
                    direction = "right"
                else : 
                    i -= 1
            
    return answer