import sys

n = int(sys.stdin.readline())
w_h = []
order_list = [1]*n

for i in range(n):
    w, h = tuple(map(int, sys.stdin.readline().split()))
    w_h.append((w,h))

for i in range(n):
    for j in range(n):
        if i != j : 
            if w_h[i][0] < w_h[j][0] and w_h[i][1] < w_h[j][1]:
                order_list[i]+=1

for ele in order_list : 
    print(ele, end = ' ')