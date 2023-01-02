import sys

s = sys.stdin.readline().rstrip()
ans =''
for c in s : 
    if 'a'<= c<='z':
        ans+=c.upper()
    elif 'A'<=c<='Z':
        ans+=c.lower()

print(ans)