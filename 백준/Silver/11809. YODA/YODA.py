import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
c_s1 = ""
c_s2 = ""
checker = dict()

s1 = s1[::-1]
s2 = s2[::-1]
n = max(len(s1), len(s2))
for i in range(n):
    if i < len(s1) and i < len(s2):
        if s1[i] > s2[i]:
            c_s1 += s1[i]
        elif s1[i] < s2[i]:
            c_s2 += s2[i]
        else:
            c_s1 += s1[i]
            c_s2 += s2[i]
    else:
        if i >= len(s1):
            c_s2 += s2[i]
        elif i >= len(s2):
            c_s1 += s1[i]

print(int(c_s1[::-1]) if c_s1 else "YODA")
print(int(c_s2[::-1]) if c_s2 else "YODA")
