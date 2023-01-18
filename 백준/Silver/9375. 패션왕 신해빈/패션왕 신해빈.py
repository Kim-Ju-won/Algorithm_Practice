import sys 

n = int(sys.stdin.readline())
for _ in range(n):
    cloth =dict()
    m = int(sys.stdin.readline())
    for _ in range(m):
        sp, name = sys.stdin.readline().split()
        if name not in cloth : 
            cloth[name] = 1
        else : 
            cloth[name]+=1
    ans = 1 
    for key in cloth : 
        ans*=(cloth[key]+1)
    ans -= 1
    print(ans)