import sys 

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    check = []
    answer = 'YES'
    for c in s : 
        if c == '(':
            check.append(c)
        else : 
            if len(check) > 0 : 
                check.pop()
            else : 
                answer='NO'
    if len(check) > 0 : 
        answer = 'NO'
    print(answer)