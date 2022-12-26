import sys 

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
answer = 0 
for i in range(n):
    answer+=int(s[i])

print(answer)