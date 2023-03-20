import sys

a,b,c,d,e,f = list(map(int, sys.stdin.readline().split()))
answer = False

for i in range(-999,1000):
    for j in range(-999,1000):
        if (a*i + b*j == c) and (d*i + e*j == f):
            print(i, j)
            answer = True
        if answer == True : 
            break
    if answer == True :
        break
