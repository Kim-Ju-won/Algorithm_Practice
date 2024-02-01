import sys

n = int(sys.stdin.readline())
if n != 0:
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort()
    k = (
        int(n * 15 / 100) + 1
        if n * 15 / 100 >= int(n * 15 / 100) + 0.5
        else int(n * 15 / 100)
    )
    arr = arr[k : len(arr) - k]
    print(
        int(sum(arr) / len(arr)) + 1
        if sum(arr) / len(arr) >= int(sum(arr) / len(arr)) + 0.5
        else int(sum(arr) / len(arr))
    )
else:
    print(0)
