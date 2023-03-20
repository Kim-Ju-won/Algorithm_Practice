import sys

n = int(sys.stdin.readline())
x_list = []
y_list = []
for _ in range(n):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()
if len(x_list) == 1 : 
    print(0)
else : 
    print((x_list[-1]-x_list[0])*(y_list[-1]-y_list[0]))