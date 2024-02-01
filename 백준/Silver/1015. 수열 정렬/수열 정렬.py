import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = [(ele, idx) for idx, ele in enumerate(arr)]
arr2.sort()
ans = [0] * n
for i in range(len(arr2)):
    ans[arr2[i][1]] = i

print(*ans)
