import sys

s = sys.stdin.readline().rstrip()
alph_dict = dict()
for i in range(97,123):
    alph_dict[chr(i)] = [0]*200000

for i in range(len(s)) : 
    alph_dict[s[i]][i]+=1
    if i != 0 :
        for key in alph_dict.keys():
            alph_dict[key][i] += alph_dict[key][i-1]

q = int(sys.stdin.readline())

for _ in range(q):
    alp, s, e = sys.stdin.readline().split()
    s = int(s)
    e = int(e)
    if s > 0 :
        print(alph_dict[alp][e]-alph_dict[alp][s-1])
    else : 
        print(alph_dict[alp][e])
