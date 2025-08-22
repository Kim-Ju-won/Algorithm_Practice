import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

n = len(s1)
m = len(s2)

a, b = max(n, m), min(n, m)

while b:
    a, b = b, a % b

lcm = n * m // a

s1 = s1 * (lcm // n)
s2 = s2 * (lcm // m)

print(1 if s1 == s2 else 0)
