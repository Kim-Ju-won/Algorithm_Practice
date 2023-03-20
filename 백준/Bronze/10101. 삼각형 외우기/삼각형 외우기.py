import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a+b+c == 180 : 
    if (a,b,c) == (60,60,60):
        print('Equilateral') 
    elif (a==b) or (b==c) or (c==a):
        print('Isosceles')
    else : 
        print('Scalene')
else:
    print('Error')