import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

ans = str(a*b*c)
ans_list = [0]*10

for ele in ans : 
    ans_list[int(ele)]+=1

for i in range(0,10):
    print(ans_list[i])