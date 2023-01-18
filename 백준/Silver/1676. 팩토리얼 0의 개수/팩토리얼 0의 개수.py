import sys 

n = int(sys.stdin.readline())
ans = 1
for i in range(1,n+1):
    ans*=i
check = str(ans)
count = 0 
for i in range(len(check)-1,-1,-1):
    if check[i] != '0':
        break
    else : 
        count+=1

print(count)