import sys 

n, m = tuple(map(int, sys.stdin.readline().split()))
s1 = set(list(map(int, sys.stdin.readline().split())))
s2 = set(list(map(int, sys.stdin.readline().split())))

s3 = (s1-s2).union(s2-s1)

print(len(s3))