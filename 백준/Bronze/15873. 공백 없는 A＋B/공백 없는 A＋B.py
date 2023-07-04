import sys

s = sys.stdin.readline().rstrip()
ans = 0
if len(s) <= 2:
    ans = int(s[0]) + int(s[1])
elif len(s) == 3:
    idx = s.find("0")
    if idx == 1:
        ans = int(s[:2]) + int(s[2])
    elif idx == 2:
        ans = int(s[0]) + int(s[1:])
elif len(s) == 4:
    ans = int(s[:2]) + int(s[2:])
print(ans)
