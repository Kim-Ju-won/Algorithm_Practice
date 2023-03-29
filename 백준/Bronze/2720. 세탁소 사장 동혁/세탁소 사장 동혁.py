import sys 

t = int(sys.stdin.readline())
denom = [25, 10, 5, 1]
for _ in range(t):
    ans = []
    money = int(sys.stdin.readline())
    for d in denom :
        ans.append(str(money//d))
        money %= d
    print(' '.join(ans))