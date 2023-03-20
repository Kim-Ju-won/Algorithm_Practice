import sys

lines = list(map(int, sys.stdin.readline().split()))

while lines != [0,0,0]:
    lines.sort()
    if lines[-1] < sum(lines[:2]):
        a, b, c = lines
        if a==b and b==c : 
            print('Equilateral')
        elif a == b or b==c or c==a : 
            print('Isosceles')
        else : 
            print('Scalene')
    else : 
        print('Invalid')
    lines = list(map(int, sys.stdin.readline().split()))

    