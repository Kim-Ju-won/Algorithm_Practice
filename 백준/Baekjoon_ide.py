import sys 

while True : 
    s = sys.stdin.readline().rstrip()
    if s[0] =='.':
        break
    check = []
    answer = 'yes'
    for c in s : 
        if c in ['(','[']:
            check.append(c)
        elif c in [')',']'] : 
            if len(check) > 0 : 
                if c == ')':
                    if check[-1] =='(':
                        check.pop()
                    else : 
                        answer='no'
                        break
                else : 
                    if check[-1] =='[':
                        check.pop()
                    else : 
                        answer='no'
                        break
            else : 
                answer='no'
                break
    if len(check) > 0 : 
        answer = 'no'
    print(answer)