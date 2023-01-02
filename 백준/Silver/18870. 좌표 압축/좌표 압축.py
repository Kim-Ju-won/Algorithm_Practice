import sys

n =int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_set = list(set(arr))
arr_set.sort()
arr_dict = dict()
for i, ele in enumerate(arr_set):
    arr_dict[ele] = i

for i in range(n):
    print(arr_dict[arr[i]], end =' ')
