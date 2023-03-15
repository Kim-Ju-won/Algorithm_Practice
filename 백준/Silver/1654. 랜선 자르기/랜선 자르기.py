import sys

def possible_lan(wire, k):
    ans = 0
    for ele in wire : 
        ans += ele // k
    return ans

n, m = tuple(map(int, sys.stdin.readline().split()))
wire = [] 

for _ in range(n):
    wire.append(int(sys.stdin.readline()))

right = max(wire)
left = 1
wire_num = 0
ans = 0
while left <= right :
    middle = (left+right)//2
    wire_num = possible_lan(wire, middle)
    if  wire_num >= m : 
        ans = max(ans, middle)
        left = middle+1
    elif wire_num < m : 
        right = middle - 1

print(ans)
