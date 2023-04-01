import sys 

start = ord('A')
num_dict = dict()

for i in range(10,36):
    num_dict[i] = chr(start)
    start+=1

n, k = tuple(map(int, sys.stdin.readline().split()))
ans = ''
while n : 
    if n%k < 10 : 
        ans+= str(n%k)
    else : 
        ans += num_dict[n%k]
    n//=k
print(ans[::-1])