import sys

t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
ans = 0
for i in range(0, t, 3):
    if i + 3 <= t:
        ans += sum(arr[i : i + 3]) - min(arr[i : i + 3])
    else:
        ans += sum(arr[i:])
print(ans)