import sys

t = int(sys.stdin.readline())
triangle = [0] * 100

for i in range(100):
    if i < 3:
        triangle[i] = 1
    else:
        triangle[i] = triangle[i - 2] + triangle[i - 3]

for i in range(t):
    print(triangle[int(sys.stdin.readline()) - 1])
