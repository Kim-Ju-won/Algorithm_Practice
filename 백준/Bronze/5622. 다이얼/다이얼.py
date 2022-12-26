import sys 

s = sys.stdin.readline().rstrip()
answer = 0

for c in s : 
    if c in 'ABC':
        answer += 3
    elif c in 'DEF':
        answer += 4
    elif c in 'GHI':
        answer += 5
    elif c in 'JKL':
        answer += 6
    elif c in 'MNO':
        answer += 7
    elif c in 'PQRS':
        answer += 8
    elif c in 'TUV':
        answer += 9
    else : 
        answer+= 10

print(answer)