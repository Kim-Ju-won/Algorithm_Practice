import sys

def cantor(line, num):
    if num == 0 : 
        print(''.join(line))
    else : 
        num-=1 
        k = 3**num
        check = True 
        for i in range(0,len(line),k):
            if check == True : 
                check = False
            else : 
                for j in range(i,i+k):
                    line[j] = ' ' 
                check=True
        cantor(line, num)

numbers = sys.stdin.readlines()
for num in numbers:
    num = int(num)
    line = ['-']*(3**num)
    cantor(line,num)