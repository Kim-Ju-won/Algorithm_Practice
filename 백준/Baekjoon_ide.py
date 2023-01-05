import sys

def draw_star(n):
    ans =[[ '*' for _ in range(n)] for _ in range(n)]
    if n == 3 : 
        k = n//3
        for i in range(k,k+k):
            for j in range(k,k+k):
                ans[i][j]=' '
        return ans
    else : 
        k = n// 3
        for i in range(0,n,k):
            for j in range(0,n,k):
                if i % n == k and j % n == k :  
                    for l in range(i,i+k):
                        for m in range(j,j+k):
                            ans[l][m] =' '
                else : 
                    temp = draw_star(k)
                    t1 = 0 
                    for l in range(i,i+k):
                        t2 = 0 
                        for m in range(j,j+k):
                            ans[l][m] =temp[t1][t2]
                            t2+=1
                        t1+=1
        return ans



n = int(sys.stdin.readline())

ans = draw_star(n)
for i in range(n):
    for j in range(n):
        print(ans[i][j], end = '')
    print()