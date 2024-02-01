import sys

t = int(sys.stdin.readline())
arr = []
for _ in range(t):
    arr.append(sys.stdin.readline().rstrip().lower())

for s in arr:
    print(s)
