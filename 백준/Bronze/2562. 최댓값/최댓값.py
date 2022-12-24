import sys

max_num = -1
idx = -1

for i in range(9):
    temp = int(sys.stdin.readline())
    if max_num < temp:
        idx = i+1
        max_num =temp

print(max_num)
print(idx)