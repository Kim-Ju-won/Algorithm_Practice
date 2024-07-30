import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque([])

for _ in range(n):
    inst = sys.stdin.readline().split()

    if inst[0] == "1":
        d.appendleft(inst[-1])
    elif inst[0] == "2":
        d.append(inst[-1])
    elif inst[0] == "3":
        print(d.popleft() if d else -1)
    elif inst[0] == "4":
        print(d.pop() if d else -1)
    elif inst[0] == "5":
        print(len(d))
    elif inst[0] == "6":
        print(0 if d else 1)
    elif inst[0] == "7":
        print(d[0] if d else -1)
    elif inst[0] == "8":
        print(d[-1] if d else -1)
