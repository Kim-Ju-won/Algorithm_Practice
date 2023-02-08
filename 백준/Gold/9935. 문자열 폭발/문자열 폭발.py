import sys

s = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
i = 0
check = []

for c in s : 
    if c == bomb[i] and i < len(bomb):
        i+=1
    elif c == bomb[0]:
        check.append(i)
        i = 1
    else : 
        check = []
        i = 0 
    stack.append(c)
    if i == len(bomb):
        for j in range(len(bomb)):
            stack.pop()
        if check : 
            i = check.pop()
        else : 
            i= 0

if stack : 
    print(''.join(stack))
else : 
    print('FRULA')