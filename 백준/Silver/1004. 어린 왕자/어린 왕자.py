import sys

t = int(sys.stdin.readline())
count_list = []

for _ in range(t):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    circle = [
        tuple(map(int, sys.stdin.readline().split())) for _ in range(n)
    ]
    count = 0 
    for c in circle : 
        x, y, r= c
        d1 = (abs(x-x1)**2 +abs(y-y1)**2)**0.5
        d2 = (abs(x-x2)**2 +abs(y-y2)**2)**0.5
        if d1 < r and d2 > r :
            count += 1 
        elif d1 > r and d2 < r :
            count += 1 
    print(count)