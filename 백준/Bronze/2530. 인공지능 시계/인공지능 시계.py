import sys 

h, m, s = tuple(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())

total = h*3600 + m *60 + s + d

print(total%(3600*24)//3600, total%3600//60, total%60)