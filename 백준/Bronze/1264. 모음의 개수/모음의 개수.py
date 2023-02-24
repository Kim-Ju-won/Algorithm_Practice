import sys 

while True : 
    s= sys.stdin.readline().rstrip()
    if s == '#':
        break
    ans = 0
    vowel = {'a','e','i','o','u','A','E','I','O','U'}
    for c in s : 
        if c in vowel : 
            ans+=1
    print(ans)