import sys 

n = int(sys.stdin.readline())
sangkun = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
sangkun_dict = dict()

for s in sangkun:
    if s in sangkun_dict : 
        sangkun_dict[s]+=1
    else : 
        sangkun_dict[s] =1

for c in card : 
    if c in sangkun_dict : 
        print(sangkun_dict[c], end =' ')
    else : 
        print(0, end = ' ')