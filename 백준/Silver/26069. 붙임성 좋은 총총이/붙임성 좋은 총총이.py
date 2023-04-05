import sys 

n = int(sys.stdin.readline())

dance = set(["ChongChong"])
for _  in range(n):
    r1, r2 = sys.stdin.readline().split()
    if r1 in dance:
        dance.add(r2)
    if r2 in dance : 
        dance.add(r1)
print(len(dance))