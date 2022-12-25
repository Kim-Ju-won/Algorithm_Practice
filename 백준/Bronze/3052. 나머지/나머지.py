import sys 

remain = [0]*42
for i in range(10):
    num = int(sys.stdin.readline()) % 42
    remain[num] += 1

print(42-remain.count(0))
