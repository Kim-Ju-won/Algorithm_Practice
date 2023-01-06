import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
chess = []
min_paint = 65
bw = [['B','W'], ['W','B']]
for i in range(n):
    chess.append(sys.stdin.readline().rstrip())

for p in bw : 
    for i in range(n-7):
        for j in range(m-7):
            paint = 0
            for l in range(i, i+8):
                for k in range(j,j+8):
                    if (l+k)%2 == 0 : 
                        if chess[l][k] != p[0]:
                            paint+=1
                    else : 
                        if chess[l][k] != p[1]:
                            paint+=1
            if min_paint > paint : 
                min_paint = paint
                

print(min_paint)