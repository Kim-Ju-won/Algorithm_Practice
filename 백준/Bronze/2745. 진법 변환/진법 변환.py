import sys

start = ord('A')
end = ord('Z')
num_dict = dict()

for i in range(start,end+1):
    num_dict[chr(i)] = i-start+10

s, k = sys.stdin.readline().split()
k = int(k)
ans = 0
for i in range(len(s)):
    if s[i] in num_dict : 
        ans+=num_dict[s[i]] * (k **(len(s)-1-i))
    else : 
        ans+=int(s[i])* (k **(len(s)-1-i))
print(ans)