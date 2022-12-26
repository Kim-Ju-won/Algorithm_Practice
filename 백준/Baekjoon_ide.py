import sys 

s = sys.stdin.readline().rstrip()
croatian_set = set(['c=', 'c-','dz=','d-','lj','nj','s=','z='])
answer = 0

for i in range(len(s)):
    if s[i] == '=' or s[i] =='-' or s[i] == 'j' : 
        if i >= 2 : 
            if s[i-2:i+1] in croatian_set : 
                answer -= 1
            elif s[i-1:i+1] not in croatian_set: 
                answer += 1
        else : 
            if s[i-1:i+1] not in croatian_set: 
                answer += 1
    else : 
        answer += 1


print(answer)