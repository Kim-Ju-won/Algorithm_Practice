import sys 

n = int(sys.stdin.readline())
square = 1 
points = 4

for i in range(1, n+1):
    if i == 1 : 
        points += 5
        square *= 2
    else : 
        points += 3*(square*square-2*(square-1)-1)+2*(square-1)*4+ 5
        square *= 2

print(points)
