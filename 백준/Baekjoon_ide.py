import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

new_arr = []
for ele in arr : 
    new_arr.append(ele)
new_arr.sort()
check = True

for i in range(n):
    if (new_arr[i]*arr[i])**0.5 != int((new_arr[i]*arr[i])**0.5 ):
        check=False
        break

if check : 
    print("YES")
else : 
    print("NO")