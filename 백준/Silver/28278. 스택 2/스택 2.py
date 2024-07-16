import sys

n = int(sys.stdin.readline())


class stack:
    def __init__(self):
        self.item = []

    def push(self, ele):
        self.item.append(ele)

    def pop(self):
        if self.item:
            return self.item.pop()
        else:
            return -1

    def __len__(self):
        return len(self.item)

    def empty(self):
        return 0 if len(self.item) else 1

    def top(self):
        return self.item[-1] if len(self.item) else -1


s = stack()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "1":
        s.push(int(cmd[1]))
    elif cmd[0] == "2":
        print(s.pop())
    elif cmd[0] == "3":
        print(len(s))
    elif cmd[0] == "4":
        print(s.empty())
    elif cmd[0] == "5":
        print(s.top())
