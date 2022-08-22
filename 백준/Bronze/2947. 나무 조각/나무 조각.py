import sys

num = sys.stdin.readline().split()
N = len(num)

while True:
    for i in range(0,N-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(num[0], num[1],num[2], num[3], num[4])
    count = 0
    for i in range(0,N-1):
        if num[i] < num[i+1]:
            count += 1
    if count == 4: 
        break
