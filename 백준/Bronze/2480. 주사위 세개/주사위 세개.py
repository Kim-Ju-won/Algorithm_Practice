import sys 

dices = list(map(int, sys.stdin.readline().split()))

if dices[0]==dices[1] and dices[1]==dices[2] : 
    print(10000 + 1000*dices[0])
elif dices[0]==dices[1] and dices[1]!=dices[2] : 
    print(1000+dices[0]*100)
elif dices[0]!=dices[1] and dices[1]==dices[2] : 
    print(1000+dices[1]*100)
elif dices[0]==dices[2] and dices[1]!=dices[2] : 
    print(1000+dices[0]*100)
else : 
    print(max(dices)*100)
