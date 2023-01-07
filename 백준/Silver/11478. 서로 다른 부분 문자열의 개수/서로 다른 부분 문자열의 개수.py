import sys 

s = sys.stdin.readline().rstrip()
n = len(s)
sub_dict = dict()

for i in range(n):
    for j in range(n-i):
        if s[j:j+i+1] in sub_dict : 
            sub_dict[s[j:j+i+1]] += 1
        else : 
            sub_dict[s[j:j+i+1]] = 1 
print(len(sub_dict.keys()))