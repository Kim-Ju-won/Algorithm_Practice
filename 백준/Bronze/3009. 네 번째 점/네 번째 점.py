import sys

x_dict = dict()
y_dict = dict()

for _ in range(3):
    x, y = tuple(map(int,sys.stdin.readline().split()))
    if x not in x_dict : 
        x_dict[x] = 1
    else : 
        x_dict[x] += 1
    if y not in y_dict : 
        y_dict[y] = 1
    else :
        y_dict[y] += 1 

x, y = 0,0

for key in x_dict.keys():
    if x_dict[key] % 2 != 0 : 
        x = key
for key in y_dict.keys():
    if y_dict[key] % 2 != 0 : 
        y = key
    
print(x,y)