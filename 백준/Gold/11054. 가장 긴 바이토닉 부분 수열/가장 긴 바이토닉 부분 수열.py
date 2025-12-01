# 바이토닉 수열
# s1 < s2 < ... < sk-1 < sk > sk+1 > ... > sn-1 > sn
# 가장 긴 바이토닉 수열을 구하기
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ascend_DP = [ 1 for _ in range(n)]
descend_DP = [1 for _ in range(n)]
DP = [ 1 for _ in range(n)]

for i in range(n):
    for j in range(0,i+1):
        if arr[i] > arr[j] : 
            ascend_DP[i] = max(ascend_DP[i], ascend_DP[j] + 1)
            
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j] : 
            descend_DP[i] = max(descend_DP[i], descend_DP[j] + 1)
        
            
for i in range(n):
    DP[i] = ascend_DP[i] + descend_DP[i]
    

print(max(DP)-1)