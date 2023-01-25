import sys

s = sys.stdin.readline()
operation = []
numbers = []
a = ''

for c in s : 
    if c == '+' or c=='-':
        operation.append(c)
        numbers.append(int(a))
        a=''
    else : 
        a+=c
numbers.append(int(a))

ans = numbers[0]
plus = 0
check = True
for i in range(len(operation)):
    if operation[i] == '+' and check == True : 
        ans+=numbers[i+1]
    elif operation[i] == '+' and check == False : 
        plus += numbers[i+1]
    elif operation[i] == '-' and check == True : 
        plus+= numbers[i+1]
        check = False
    else : 
        ans-=plus 
        plus = numbers[i+1]
ans-=plus

print(ans)