import sys

n = map(int, sys.stdin.readline().split())
answer = "S"
for c in n:
    if c != 0 and c != 1:
        answer = "F"
        break

print(answer)
