import sys 

s = sys.stdin.readline().rstrip().upper()
s_dict = dict()
answer = []
check = -1
for c in s : 
    if c not in s_dict : 
        s_dict[c] = 1 
    else : 
        s_dict[c] += 1

for key in s_dict.keys():
    if s_dict[key] > check :
        check =  s_dict[key]
        answer = [key]
    elif s_dict[key] == check : 
        answer.append(key)

if len(answer) > 1 : 
    print('?')
else : 
    print(answer[0])