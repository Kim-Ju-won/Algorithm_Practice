import sys

arr = []

for _ in range(5):
    ele = int(sys.stdin.readline())
    arr.append(ele)
arr.sort()
print(sum(arr)//len(arr))
print(arr[len(arr)//2])