import sys


class Set:
    def __init__(self):
        self.s = set([])

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        if x in self.s:
            self.s.remove(x)

    def check(self, x):
        return 1 if x in self.s else 0

    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = set([i for i in range(1, 21)])

    def empty(self):
        self.s = set([])


n = int(sys.stdin.readline())
s = Set()
for _ in range(n):
    inst = sys.stdin.readline().split()

    if inst[0] == "add":
        s.add(int(inst[1]))
    elif inst[0] == "check":
        print(s.check(int(inst[1])))
    elif inst[0] == "remove":
        s.remove(int(inst[1]))
    elif inst[0] == "toggle":
        s.toggle(int(inst[1]))
    elif inst[0] == "empty":
        s.empty()
    elif inst[0] == "all":
        s.all()
