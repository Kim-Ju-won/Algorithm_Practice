import sys

n = int(sys.stdin.readline())
stack = []
check_list = []
push_pop = []
for _ in range(n):
    check_list.append(int(sys.stdin.readline()))

num = 1
idx = 0
while num <= n : 
    if len(stack) == 0 : 
        stack.append(num)
        push_pop.append('+')
        num+=1
    else : 
        if stack[-1] != check_list[idx] : 
            stack.append(num)
            num+=1
            push_pop.append('+')
        else : 
            stack.pop()
            idx+=1
            push_pop.append('-')

for i in range(idx,n):
    if check_list[i] == stack[-1]:
        stack.pop()
        push_pop.append('-')
if len(stack) == 0 : 
    for ele in push_pop:
        print(ele)
else : 
    print('NO')

