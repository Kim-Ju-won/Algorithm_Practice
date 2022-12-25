import sys 

def diff(num):
    num = str(num)
    diff = 0 
    if len(num) >= 3 : 
        diff = int(num[1]) - int(num[0])
        for i in range(1, len(num)-1) : 
            if diff != (int(num[i+1])-int(num[i])):
                return False
    return True

def solve(num):
    count = 0
    for i in range(1,num+1):
        if diff(i):
            count+=1
    return count

n = int(sys.stdin.readline())
print(solve(n))