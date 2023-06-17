import sys

s = sys.stdin.readline().rstrip()
alp_dict = dict()
for i in range(97, 123):
    alp_dict[chr(i)] = 0

for c in s:
    alp_dict[c] += 1

for _, value in alp_dict.items():
    print(value, end=" ")
