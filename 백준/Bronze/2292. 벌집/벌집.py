import sys 

a = int(sys.stdin.readline())
count = 0
check = 1
while a > check :
    count+=1
    check += 6*count

print(count+1)
