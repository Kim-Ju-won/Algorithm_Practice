import sys 

s = sys.stdin.readline().rstrip()
alphabet= [-1]*26
for i in range(len(s)):
    alp = ord(s[i])-97
    if alphabet[alp] == -1 or i < alphabet[alp] : 
        alphabet[alp] = i

for ele in alphabet : 
    print(ele, end=' ')
