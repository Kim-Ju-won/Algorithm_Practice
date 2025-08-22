import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = set(map(int, sys.stdin.readline().split()))

new_set = set([i for i in range(1, n + 1)])

if n != m:
    answer = list(new_set - arr)
    answer.sort()
    for ele in answer:
        print(ele, end=" ")
else:
    print("*")
