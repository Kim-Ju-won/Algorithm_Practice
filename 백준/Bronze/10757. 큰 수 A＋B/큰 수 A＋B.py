import sys 

a, b = list(sys.stdin.readline().split())
answer = []

a = a[::-1]
b = b[::-1]
n = max(len(a),len(b))
carry = 0
a_temp = 0 
b_temp = 0

for i in range(n):
    if i < len(a) : 
        a_temp=int(a[i])
    else : 
        a_temp = 0 

    if i < len(b) : 
        b_temp=int(b[i])
    else : 
        b_temp = 0

    temp = a_temp+b_temp+carry
    carry = temp//10
    temp %= 10 
    answer.append(str(temp))
if carry != 0 : 
    answer.append(str(carry))
print(''.join(answer[::-1]))
