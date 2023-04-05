import sys 

n = int(sys.stdin.readline())

gom_set = set()
ans = 0
for _  in range(n):
    s = sys.stdin.readline().rstrip()
    if s == "ENTER":
        gom_set = set()
    else : 
        if s not in gom_set:
            ans+=1
            gom_set.add(s)

print(ans)