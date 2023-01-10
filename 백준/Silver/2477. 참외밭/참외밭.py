import sys

n = int(sys.stdin.readline())

x_dict = dict()
y_dict = dict()
d_dict = dict()
x, y = 0,0

for i in range(6):
    d, num  = tuple(map(int, sys.stdin.readline().split()))
    if d in d_dict : 
        d_dict[d] += 1
    else : 
        d_dict[d] = 1

    if d == 1 : 
        x+=num
    elif d == 2 : 
        x-=num
    elif d == 3 : 
        y-=num
    else : 
        y+=num 
    
    if x not in x_dict : 
        x_dict[x] = 1
    else  :
        x_dict[x] += 1
    if y not in y_dict : 
        y_dict[y] = 1
    else  :
        y_dict[y] += 1

w = list(x_dict.keys())
h = list(y_dict.keys())
min_w = abs(min(w))
min_h = abs(min(h))
for i in range(len(w)):
    w[i]+= min_w
    h[i]+= min_h
w.sort()
h.sort()

if d_dict[3] == 2 and d_dict[1] ==2 :  
    print(n*((w[2]-w[0])*(h[2]-h[0])-w[1]*h[1]))
elif d_dict[4] == 2 and d_dict[2] ==2 :  
    print(n*((w[2]-w[0])*(h[2]-h[0])-(w[2]-w[1])*(h[2]-h[1])))
elif d_dict[4] == 2 and d_dict[1] ==2 :  
    print(n*((w[2]-w[0])*(h[2]-h[0])-(w[2]-w[1])*(h[1])))
elif d_dict[3] == 2 and d_dict[2] ==2 :  
    print(n*((w[2]-w[0])*(h[2]-h[0])-(w[1])*(h[2]-h[1])))
