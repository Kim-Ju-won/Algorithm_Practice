import sys 

n = int(sys.stdin.readline())
min_bag = [-1 for _ in range(n+1)]

for i in range(1,n+1):
    if i >=3 : 
        temp1 = i//3 if i%3 == 0 else n+1
        temp2 = i//5 if i%5 == 0 else n+1
        temp3 = min_bag[i-3]+1 if min_bag[i-3] != -1 else n+1
        temp4 = min_bag[i-5]+1 if min_bag[i-5] != -1 else n+1
        min_bag[i] = min(temp1, temp2, temp3, temp4)
        if min_bag[i] == n+1 : 
            min_bag[i] = -1
print(min_bag[n])
