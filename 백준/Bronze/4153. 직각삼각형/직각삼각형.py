import sys

while True : 
    a, b, c = tuple(map(int, sys.stdin.readline().split()))
    if (a, b, c) == (0,0,0):
        break
    else : 
        max_num = max(a,b,c)
        other_num = []
        for ele in (a,b,c):
            if ele != max_num : 
                other_num.append(ele)
        if max(a,b,c)**2 == other_num[0]**2 + other_num[1]**2 : 
            print('right')
        else  :
            print('wrong')